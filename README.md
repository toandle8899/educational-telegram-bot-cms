# Educational Telegram Bot with CMS

An AI-powered educational bot that delivers personalized learning content, interactive quizzes, and intelligent conversations to help users master Statistics. The bot includes a comprehensive Content Management System (CMS) for administrators.

## Features

### Bot Features
- 📚 Scheduled delivery of educational videos
- ✍️ Interactive quizzes with automated grading
- 🤖 AI-powered chat using Perplexity API
- 📊 Progress tracking and weekly summaries
- ⏰ Customizable learning schedules

### CMS Features
- 📝 Content management for videos and quizzes
- 📈 Detailed analytics dashboard
- 👥 User engagement monitoring
- ⚙️ Bot message customization
- 🔍 Chat history analysis

## Technology Stack

- **Backend:**
  - Python 3.8+
  - python-telegram-bot
  - Flask (CMS)
  - Google Sheets API (Database)
  - Perplexity API (AI Chat)

- **Frontend:**
  - Bootstrap 5
  - Chart.js
  - Font Awesome
  - Google Fonts

## Prerequisites

1. Python 3.8 or higher
2. pip (Python package manager)
3. Google Cloud account with Sheets API enabled
4. Telegram Bot Token
5. Perplexity API Token

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd educational-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file with your credentials:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
PERPLEXITY_API_TOKEN=your_perplexity_api_token
GOOGLE_CLOUD_CLIENT_ID=your_google_cloud_client_id
GOOGLE_CLOUD_CLIENT_SECRET=your_google_cloud_client_secret
FLASK_SECRET_KEY=your_flask_secret_key
```

## Google Sheets Setup

1. Create a new Google Sheets document with the following sheets:
   - Videos (columns: id, url, title, description, sequence_order)
   - Quizzes (columns: id, video_id, question, options, correct_option_id)
   - Users (columns: user_id, progress, preferred_hour, join_date)
   - QuizResponses (columns: user_id, quiz_id, is_correct, timestamp)
   - ChatHistory (columns: user_id, query, response, timestamp)
   - Settings (columns: key, value)

2. Share the spreadsheet with your Google Cloud service account email

## Running the Application

### Running the Bot Only
```bash
python run.py bot
```

### Running the CMS Only
```bash
python run.py cms
```

### Running Both Services
```bash
python run.py both
```

### Additional Options
- `--host`: Specify the host for CMS (default: 0.0.0.0)
- `--port`: Specify the port for CMS (default: 5000)
- `--debug`: Run in debug mode

## Digital Ocean Deployment

1. Create a new Digital Ocean droplet:
   - Choose Ubuntu 22.04 LTS
   - Select appropriate size (minimum 2GB RAM recommended)
   - Add SSH key for secure access

2. Connect to your droplet:
```bash
ssh root@your_droplet_ip
```

3. Update system and install requirements:
```bash
apt update && apt upgrade -y
apt install -y python3-pip python3-venv nginx supervisor
```

4. Clone repository and setup:
```bash
cd /opt
git clone <repository-url> educational-bot
cd educational-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. Create supervisor configuration:
```bash
nano /etc/supervisor/conf.d/educational-bot.conf
```

Add the following content:
```ini
[program:telegram-bot]
command=/opt/educational-bot/venv/bin/python run.py bot
directory=/opt/educational-bot
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/supervisor/telegram-bot.err.log
stdout_logfile=/var/log/supervisor/telegram-bot.out.log

[program:cms]
command=/opt/educational-bot/venv/bin/python run.py cms
directory=/opt/educational-bot
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/supervisor/cms.err.log
stdout_logfile=/var/log/supervisor/cms.out.log
```

6. Configure Nginx:
```bash
nano /etc/nginx/sites-available/educational-bot
```

Add the following content:
```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

7. Enable the site and restart services:
```bash
ln -s /etc/nginx/sites-available/educational-bot /etc/nginx/sites-enabled/
supervisorctl reread
supervisorctl update
supervisorctl start all
service nginx restart
```

8. Setup SSL with Certbot:
```bash
apt install certbot python3-certbot-nginx
certbot --nginx -d your_domain.com
```

## Monitoring & Maintenance

### Viewing Logs
- Bot logs: `/var/log/supervisor/telegram-bot.out.log`
- CMS logs: `/var/log/supervisor/cms.out.log`
- Error logs: `/var/log/supervisor/telegram-bot.err.log` and `/var/log/supervisor/cms.err.log`

### Backup
Regular backups of the Google Sheets database are recommended. You can set up automated backups using Google Apps Script.

### Updating
To update the application:
```bash
cd /opt/educational-bot
git pull
supervisorctl restart all
```

## Security Considerations

1. Keep your `.env` file secure and never commit it to version control
2. Regularly update your dependencies
3. Use strong passwords for the CMS admin interface
4. Monitor server logs for suspicious activity
5. Keep your system and packages up to date
6. Configure firewall rules appropriately

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
