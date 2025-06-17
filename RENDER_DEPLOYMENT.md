# Deployment Guide for Educational Bot CMS on Render.com

This guide will help you deploy the Educational Bot CMS (Flask app) on Render.com, a modern cloud platform that simplifies app deployment without server management.

---

## Prerequisites

- Render.com account: https://render.com/
- GitHub repository with your CMS code pushed
- Basic knowledge of Git and GitHub

---

## Step 1: Prepare your project

1. Ensure your project has a `requirements.txt` file listing all Python dependencies:

```bash
pip freeze > requirements.txt
```

2. Create a `Procfile` in the project root with the following content:

```
web: gunicorn cms.app:app
```

This tells Render how to start your app.

3. Modify `cms/app.py` to use the port provided by Render:

```python
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

---

## Step 2: Push your code to GitHub

Make sure your latest code is committed and pushed to a GitHub repository.

---

## Step 3: Create a new Web Service on Render

1. Log in to Render.com.

2. Click "New" > "Web Service".

3. Connect your GitHub account and select your CMS repository.

4. Configure the service:

- Environment: Python 3
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn cms.app:app`
- Region: Choose your preferred region

5. Click "Create Web Service".

Render will start building and deploying your app.

---

## Step 4: Set Environment Variables

In your Render service dashboard:

1. Go to the "Environment" tab.

2. Add the following environment variables with your actual secrets:

- TELEGRAM_BOT_TOKEN
- PERPLEXITY_API_TOKEN
- GOOGLE_CLOUD_CLIENT_ID
- GOOGLE_CLOUD_CLIENT_SECRET
- FLASK_SECRET_KEY
- ADMIN_USERNAME
- ADMIN_PASSWORD
- SPREADSHEET_URL

---

## Step 5: Access your CMS

Once deployment is complete, Render will provide a public URL for your CMS.

Visit the URL in your browser to access the CMS login page.

---

## Step 6: Monitor Logs and Manage Service

- Use the Render dashboard to view logs, restart the service, and manage settings.

---

# Notes

- Render offers free tier with limitations suitable for development and small projects.
- For production, consider upgrading your plan and securing your environment variables.
- You can enable HTTPS automatically via Render.

---

This guide helps you deploy the Educational Bot CMS on Render.com with minimal setup and no server management.

If you want, I can help you automate this deployment or troubleshoot any issues.
