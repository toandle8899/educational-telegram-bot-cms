#!/usr/bin/env python3
import sys
import os
import argparse
from logger import log_info, log_error, bot_logger, cms_logger

def setup_environment():
    """Setup environment variables and check requirements"""
    try:
        # Check if .env file exists
        if not os.path.exists('.env'):
            print("Warning: .env file not found. Using default configuration.")
        
        # For CMS, we only require FLASK_SECRET_KEY
        if len(sys.argv) > 1 and sys.argv[1] == 'cms':
            if not os.getenv('FLASK_SECRET_KEY'):
                os.environ['FLASK_SECRET_KEY'] = 'dev-secret-key'
                print("Warning: Using development secret key. Do not use in production!")
            return True
            
        # For bot, verify all required environment variables
        required_vars = [
            'TELEGRAM_BOT_TOKEN',
            'PERPLEXITY_API_TOKEN',
            'GOOGLE_CLOUD_CLIENT_ID',
            'GOOGLE_CLOUD_CLIENT_SECRET'
        ]
        
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables for bot: {', '.join(missing_vars)}")
            
        return True
    except Exception as e:
        print(f"Error setting up environment: {str(e)}")
        return False

def run_bot():
    """Start the Telegram bot"""
    try:
        from bot.bot import EducationalBot
        log_info(bot_logger, "Starting Telegram bot...")
        
        bot = EducationalBot()
        bot.run()
        
    except Exception as e:
        log_error(bot_logger, f"Error starting bot: {str(e)}", exc_info=True)
        sys.exit(1)

def run_cms(host='0.0.0.0', port=5000, debug=False):
    """Start the CMS web application"""
    try:
        from cms.app import app
        log_info(cms_logger, f"Starting CMS on {host}:{port}...")
        
        app.run(host=host, port=port, debug=debug)
        
    except Exception as e:
        log_error(cms_logger, f"Error starting CMS: {str(e)}", exc_info=True)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Run Educational Bot or CMS')
    parser.add_argument('service', choices=['bot', 'cms', 'both'], 
                       help='Service to run (bot, cms, or both)')
    parser.add_argument('--host', default='0.0.0.0', 
                       help='Host for CMS (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=5000, 
                       help='Port for CMS (default: 5000)')
    parser.add_argument('--debug', action='store_true', 
                       help='Run in debug mode')
    
    args = parser.parse_args()
    
    # Setup environment
    if not setup_environment():
        sys.exit(1)
    
    if args.service == 'both':
        # Run both services using multiprocessing
        from multiprocessing import Process
        
        bot_process = Process(target=run_bot)
        cms_process = Process(target=run_cms, 
                            kwargs={'host': args.host, 'port': args.port, 'debug': args.debug})
        
        try:
            bot_process.start()
            cms_process.start()
            
            bot_process.join()
            cms_process.join()
            
        except KeyboardInterrupt:
            print("\nShutting down services...")
            bot_process.terminate()
            cms_process.terminate()
            bot_process.join()
            cms_process.join()
            
    elif args.service == 'bot':
        run_bot()
    else:  # cms
        run_cms(host=args.host, port=args.port, debug=args.debug)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)
