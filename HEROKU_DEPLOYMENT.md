# Deployment Guide for Educational Bot CMS on Heroku

This guide will help you deploy the Educational Bot CMS (Flask app) on Heroku, a cloud platform that abstracts server management.

---

## Prerequisites

- Heroku account: https://signup.heroku.com/
- Heroku CLI installed: https://devcenter.heroku.com/articles/heroku-cli
- Git installed and your project in a git repository

---

## Step 1: Prepare your project for Heroku

1. Ensure you have a `requirements.txt` file listing all Python dependencies:

```bash
pip freeze > requirements.txt
```

2. Create a `Procfile` in the project root with the following content:

```
web: gunicorn cms.app:app
```

This tells Heroku how to run your app.

3. Ensure your Flask app listens on the port provided by Heroku:

Modify `cms/app.py` to use the environment variable `PORT`:

```python
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

---

## Step 2: Initialize git and commit your code

```bash
git init
git add .
git commit -m "Prepare app for Heroku deployment"
```

---

## Step 3: Create a Heroku app and push your code

```bash
heroku login
heroku create your-app-name
git push heroku main
```

Replace `your-app-name` with a unique name.

---

## Step 4: Set environment variables on Heroku

Set your secrets and config vars:

```bash
heroku config:set TELEGRAM_BOT_TOKEN=your_token
heroku config:set PERPLEXITY_API_TOKEN=your_token
heroku config:set GOOGLE_CLOUD_CLIENT_ID=your_client_id
heroku config:set GOOGLE_CLOUD_CLIENT_SECRET=your_client_secret
heroku config:set FLASK_SECRET_KEY=your_flask_secret
heroku config:set ADMIN_USERNAME=admin
heroku config:set ADMIN_PASSWORD=admin123
heroku config:set SPREADSHEET_URL=your_spreadsheet_url
```

---

## Step 5: Scale the dynos and open your app

```bash
heroku ps:scale web=1
heroku open
```

---

## Step 6: Monitor logs

```bash
heroku logs --tail
```

---

# Notes

- Heroku provides a free tier with limitations.
- Use Heroku Add-ons for databases or other services if needed.
- For persistent storage, use external services like AWS S3 or databases.

---

This guide helps you deploy the Educational Bot CMS on Heroku without managing servers.

If you want, I can help you automate this deployment or troubleshoot issues.
