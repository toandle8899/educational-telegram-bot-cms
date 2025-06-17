# Deployment Guide for Educational Bot CMS on DigitalOcean

This guide will help you deploy the Educational Bot CMS (Flask app) on DigitalOcean using a Droplet (Ubuntu server).

---

## Prerequisites

- DigitalOcean account
- Domain name (optional, for production)
- Basic knowledge of SSH and Linux commands

---

## Step 1: Create a Droplet

1. Log in to your DigitalOcean account.
2. Create a new Droplet with Ubuntu 22.04 LTS.
3. Choose a plan (Basic plan with 1GB RAM is sufficient for testing).
4. Add your SSH key or use password authentication.
5. Create the Droplet and note its public IP address.

---

## Step 2: Connect to the Droplet using PuTTY

1. Download and install PuTTY from https://www.putty.org/ if you haven't already.

2. Open PuTTY.

3. In the "Host Name (or IP address)" field, enter your Droplet's public IP address.

4. Ensure the Port is set to 22 and Connection type is set to SSH.

5. (Optional) In the "Category" pane on the left, go to Connection > SSH > Auth to load your private key file (.ppk) if you use key-based authentication.

6. Click "Open" to start the SSH session.

7. When prompted, enter your username (usually `root`) and press Enter.

8. If this is your first time connecting, PuTTY will ask you to confirm the server's host key. Click "Yes" to continue.

You are now connected to your DigitalOcean Droplet via PuTTY.

```bash
ssh root@your_droplet_ip
```


---

## Step 3: Update and install dependencies (Simplified)

You can run a single command to update your server and install all required packages in one step:

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y python3 python3-pip python3-venv git nginx
```

This command will:

- Update the package list
- Upgrade all installed packages
- Install Python 3, pip, virtual environment support, git, and Nginx

This is the easiest way to prepare your server for deploying the CMS application.


---

## Step 4: Clone your project repository

If your project is on GitHub or other git hosting:

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

If not, you can upload your project files via SCP or SFTP.

---

## Step 5: Set up Python virtual environment and install requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Step 6: Configure environment variables

Create a `.env` file in the project root with the required environment variables:

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
PERPLEXITY_API_TOKEN=your_perplexity_api_token
GOOGLE_CLOUD_CLIENT_ID=your_google_client_id
GOOGLE_CLOUD_CLIENT_SECRET=your_google_client_secret
FLASK_SECRET_KEY=your_flask_secret_key
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
SPREADSHEET_URL=your_google_sheet_url
```

---

## Step 7: Test the application

Run the Flask app to verify it works:

```bash
source venv/bin/activate
python3 run.py cms
```

Visit `http://your_droplet_ip:5000` in your browser.

---

## Step 8: Set up Gunicorn and systemd service

Install Gunicorn:

```bash
pip install gunicorn
```

Create a systemd service file `/etc/systemd/system/educational_bot_cms.service`:

```
[Unit]
Description=Educational Bot CMS
After=network.target

[Service]
User=root
WorkingDirectory=/root/yourrepo
EnvironmentFile=/root/yourrepo/.env
ExecStart=/root/yourrepo/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 cms.app:app

[Install]
WantedBy=multi-user.target
```

Reload systemd and start the service:

```bash
systemctl daemon-reload
systemctl start educational_bot_cms
systemctl enable educational_bot_cms
```

---

## Step 9: Configure Nginx as a reverse proxy

Create Nginx config `/etc/nginx/sites-available/educational_bot_cms`:

```
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable the site and restart Nginx:

```bash
ln -s /etc/nginx/sites-available/educational_bot_cms /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

---

## Step 10: Access your CMS

Visit `http://your_domain_or_ip` in your browser.

---

## Optional: Enable HTTPS with Let's Encrypt

Use Certbot to enable HTTPS:

```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d your_domain
```

---

# Summary

This guide helps you deploy the Educational Bot CMS on DigitalOcean with Gunicorn and Nginx. Adjust paths and variables as needed.

If you want, I can help you create deployment scripts or automate this process.
