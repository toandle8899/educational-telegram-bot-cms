# Super Easy Guide to Deploy Your CMS on Render.com - Part 2 🚀

## Step 4: Add Your Secret Information 🔑

1. On your web service page, click "Environment" in the left menu
2. Click "Add Environment Variable"
3. Add these one by one:
   - TELEGRAM_BOT_TOKEN = your_bot_token
   - PERPLEXITY_API_TOKEN = your_api_token
   - GOOGLE_CLOUD_CLIENT_ID = your_client_id
   - GOOGLE_CLOUD_CLIENT_SECRET = your_client_secret
   - FLASK_SECRET_KEY = make_up_a_random_string
   - ADMIN_USERNAME = pick_your_username
   - ADMIN_PASSWORD = pick_your_password
   - SPREADSHEET_URL = your_google_sheet_url
4. Click "Save Changes"

## Step 5: Watch It Build! 🏗️

1. Go to the "Events" tab
2. Watch the progress as Render builds your app
3. Wait until you see "Deploy succeeded"

## Step 6: Visit Your Website! 🎉

1. Look at the top of your Render dashboard
2. Find the URL that looks like `https://your-cms-name.onrender.com`
3. Click it or copy-paste into your browser
4. You should see your CMS login page!

## If Something Goes Wrong 🔧

1. Check the "Logs" tab in Render
2. Look for any red error messages
3. Make sure all your environment variables are set correctly
4. Try clicking "Manual Deploy" > "Deploy latest commit"

## Need More Help? 🤔

1. Check if your code works locally first
2. Make sure your `requirements.txt` has all needed packages
3. Check if your GitHub repository has all the latest code

Remember: The first deploy might take a few minutes, so be patient! ⏳

---

Want me to help you with any of these steps? Just ask! 😊
