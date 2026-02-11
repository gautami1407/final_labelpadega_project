# 🚀 Deployment Guide - Streamlit Cloud

This guide walks you through deploying the Label Padega Sabh application to Streamlit Cloud.

---

## ✅ Pre-Deployment Checklist

- [ ] Code is pushed to GitHub
- [ ] All files are in the repository (except `.env`)
- [ ] `requirements.txt` is updated
- [ ] `.streamlit/config.toml` exists
- [ ] `.gitignore` includes `.env` and `secrets.toml`
- [ ] API keys are ready (Gemini, USDA)

---

## 📋 Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Initialize Git** (if not done):
   ```bash
   git init
   git add .
   git commit -m "Convert Flask app to Streamlit"
   ```

2. **Create `.gitignore`** (already created in this project):
   ```
   .env
   .streamlit/secrets.toml
   __pycache__/
   *.pyc
   ```

3. **Verify files in Git**:
   ```bash
   git status
   # Should NOT show .env or secrets.toml
   ```

### Step 2: Push to GitHub

1. Create a new repository on GitHub
2. Add remote and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/label-padega-sabh.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Deploy on Streamlit Cloud

1. **Visit Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub account

2. **Create New App**:
   - Click "New App"
   - Select your GitHub repository
   - Select branch: `main`
   - Select file: `main.py`
   - Click "Deploy"

3. **Wait for Deployment**:
   - Streamlit will install dependencies from `requirements.txt`
   - This takes 2-3 minutes
   - You'll see logs in real-time

### Step 4: Configure Secrets

1. **Open App Settings**:
   - Click the hamburger menu (≡) in top right
   - Select "Settings"

2. **Go to Secrets Section**:
   - Click on "Secrets" tab
   - Add your secrets in TOML format:

   ```toml
   gemini_api_key = "your_gemini_key_here"
   usda_api_key = "your_usda_key_here"
   ```

3. **Save Secrets**:
   - Close the settings
   - App will automatically restart

### Step 5: Monitor and Test

1. **Check App Status**:
   - Wait for "Your app is loading..."
   - Should see "✓ App is running" in 1-2 minutes

2. **Test All Features**:
   - Navigate through all sidebar options
   - Test file uploads
   - Verify API calls work
   - Check chat functionality

---

## 📊 Environment Variables

### Streamlit Cloud Integration

In `.streamlit/secrets.toml` (for production):

```toml
# Google Gemini API
gemini_api_key = "AIza..."

# USDA FDC API (optional)
usda_api_key = "NwTn..."

# Other settings
[database]
host = "your-db-host"
user = "your-db-user"
password = "your-db-password"
```

### Accessing in Code

```python
import streamlit as st

# Access secrets
gemini_key = st.secrets["gemini_api_key"]

# With defaults
usda_key = st.secrets.get("usda_api_key", "default_value")
```

---

## 🔧 Troubleshooting Deployment

### App keeps restarting

**Cause**: Error in code or missing dependencies

**Solution**:
1. Check the logs (click icon in top right)
2. Look for error messages
3. Fix and push changes:
   ```bash
   git add .
   git commit -m "Fix issue"
   git push origin main
   ```
4. Streamlit auto-redeploys on push

### "Module not found" error

**Cause**: Missing dependency

**Solution**:
1. Add to `requirements.txt`
2. Push changes
3. App will auto-update

### API key errors

**Cause**: Secrets not properly configured

**Solution**:
1. Verify secrets in Settings > Secrets
2. Check spelling matches your code
3. Ensure keys are valid
4. Wait 1-2 minutes for changes to take effect

### App is very slow

**Cause**: Inefficient caching or API limits

**Solution**:
```python
# Add caching to expensive operations
@st.cache_data(ttl=3600)  # Cache for 1 hour
def expensive_function():
    return result

# Disable stats gathering
# Already in config.toml
```

---

## 🔐 Security Best Practices

1. **Never Commit Secrets**:
   ```bash
   # Verify before pushing
   git status
   # Should NOT list .env or secrets.toml
   ```

2. **Use Strong API Keys**:
   - Generate new keys for production
   - Rotate keys periodically
   - Don't share keys publicly

3. **Monitor API Usage**:
   - Check Google Cloud Console for Gemini usage
   - Set up billing alerts
   - Monitor API quotas

4. **Secure App Access**:
   - Use custom domain (paid plan feature)
   - Enable authentication if needed
   - Monitor access logs

---

## 📈 Scaling & Performance

### For Free Tier:
- ✅ Good for development and small teams
- ✅ Up to 3 deployments
- ⚠️ Resets inactivity after 30 minutes

### Upgrade to Pro:
- Runs continuously
- Custom domain
- Private apps
- Priority support
- Starting at $10/month

### Optimization Tips:
```python
# Use caching liberally
@st.cache_data(ttl=3600)
def load_data():
    return data

# Lazy load modules
try:
    import module
except ImportError:
    st.error("Module not installed")

# Optimize images
from PIL import Image
img = Image.open("path")
img.thumbnail((800, 800))
```

---

## 🔄 Continuous Deployment

### Auto-Deploy on Git Push

Streamlit Cloud automatically:
1. Detects changes on GitHub
2. Pulls latest code
3. Installs dependencies
4. Restarts app

**No manual deployment needed!**

---

## 💾 Database Setup (Optional)

If you want to add persistent storage:

### PostgreSQL Database:
```python
import psycopg2
import streamlit as st

@st.cache_resource
def init_connection():
    return psycopg2.connect(
        **st.secrets["postgres"]
    )

conn = init_connection()
```

Secrets configuration:
```toml
[postgres]
host = "your-host"
database = "your-db"
user = "your-user"
password = "your-password"
```

---

## 📊 Monitoring & Analytics

### App Metrics:
- Check logs: App menu > Manage app > View logs
- Monitor resource usage
- Track error rates
- View user activity

### Set Up Alerts:
- Enable email notifications for errors
- Use external monitoring (Sentry, etc.)
- Track API usage limits

---

## 🎯 Custom Domain Setup

### For Pro Plan Users:

1. **Add Custom Domain**:
   - Go to App settings
   - Custom domain section
   - Add your domain (e.g., `label-padega.com`)

2. **Configure DNS**:
   - CNAME: `your-app.streamlitapp.com`
   - Add to your DNS provider

3. **Verify**:
   - Takes 5-10 minutes to propagate
   - Automatic HTTPS setup

---

## 🆘 Support & Resources

- **Streamlit Docs**: https://docs.streamlit.io/deploy
- **Cloud FAQ**: https://streamlit.io/cloud
- **Community Forum**: https://discuss.streamlit.io
- **Status Page**: https://status.streamlit.io

---

## 📅 Maintenance

### Regular Tasks:
- [ ] Monitor logs weekly
- [ ] Update dependencies monthly
- [ ] Review API usage
- [ ] Test all features
- [ ] Backup important data

### Update Procedure:
1. Test locally: `streamlit run main.py`
2. Commit changes: `git commit -m "Update message"`
3. Push: `git push origin main`
4. Verify deployment
5. Test in production

---

## ✨ After Deployment

### Share Your App:
```
Share URL: https://your-org-label-padega.streamlit.app
```

### Set Up Custom Logo:
```python
# In main.py
st.set_page_config(
    page_icon="🍎",
    # ... other config
)
```

### Add Analytics:
```python
import streamlit as st

# Track page views
st.session_state.page_views = st.session_state.get("page_views", 0) + 1
```

---

## 🎉 Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] App deployed to Streamlit Cloud
- [ ] Secrets configured
- [ ] All features tested
- [ ] Custom domain set (optional)
- [ ] Monitoring enabled
- [ ] Shared with team
- [ ] Documentation updated

---

**Deployment Status**: Ready for Production ✅
**Last Updated**: February 11, 2026
