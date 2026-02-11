# 🆘 Common Tasks & Troubleshooting

This guide covers common questions and tasks you might encounter. **Start here if something doesn't work!**

---

## ❓ Common Questions

### Q1: Where do I put my API keys?

**A**: Create a `.env` file in the project root:

```bash
# Create from template
cp .env.example .env

# Edit with your keys
nano .env  # or use your favorite editor
```

Content:
```env
GEMINI_API_KEY=your_gemini_key_here
USDA_API_KEY=your_usda_key_here
```

**Important**: Never commit `.env` to Git! It's in `.gitignore`.

---

### Q2: How do I run the app?

**A**: Simple!

```bash
cd project
pip install -r requirements.txt  # First time only
streamlit run main.py
```

Then open `http://localhost:8501` in your browser.

---

### Q3: How do I add a new feature?

**A**: 
1. Create `pages/myfeature.py`:
   ```python
   import streamlit as st
   
   def run_my_feature():
       st.markdown("### 🎯 My Feature")
       st.write("Content here...")
   ```

2. Add to sidebar in `main.py`:
   ```python
   nav_options = {
       # ...existing...
       "🎯 My Feature": "My_Feature",
   }
   ```

3. Add routing in `main.py`:
   ```python
   elif st.session_state.page == "My_Feature":
       from pages.myfeature import run_my_feature
       run_my_feature()
   ```

---

### Q4: How do I customize the theme?

**A**: Edit these files:

**For colors**:
- `.streamlit/config.toml` - Change `[theme]` section
- Or: `main.py` - Edit CSS `st.markdown("""<style>...`

**For layout**:
- `main.py` - Edit HTML/CSS in `st.markdown()`

---

### Q5: Can I use a database?

**A**: Yes! Add connection:

```python
import sqlite3
# or
import sqlalchemy as sql
import psycopg2

# Then add to pages as needed
```

See `ARCHITECTURE.md` for database example.

---

### Q6: How do I deploy to production?

**A**: See `DEPLOYMENT.md` for complete guide. Quick version:

1. Push to GitHub
2. Go to share.streamlit.io
3. Deploy from GitHub
4. Add secrets

---

### Q7: What if I get "ModuleNotFoundError"?

**A**: Missing package. Solutions:

```bash
# 1. Install missing package
pip install package_name

# 2. Add to requirements.txt
echo "package_name" >> requirements.txt

# 3. Install all requirements
pip install -r requirements.txt

# 4. Restart your app
# Kill current: Ctrl+C
# Restart: streamlit run main.py
```

---

### Q8: My changes aren't showing up?

**A**: Streamlit caches files. Solutions:

```bash
# 1. Hard refresh browser (Ctrl+Shift+R)

# 2. Clear Streamlit cache
streamlit cache clear

# 3. Restart app
# Kill: Ctrl+C
# Restart: streamlit run main.py

# 4. Check file is saved (Ctrl+S)
```

---

### Q9: Can I share my app without deploying?

**A**: Temporary solution:

```bash
# 1. Run locally: streamlit run main.py

# 2. Share URL: http://your-ip:8501
#    (both computers on same network)

# 3. For permanent: Deploy to Streamlit Cloud
```

---

### Q10: How do I add authentication?

**A**: Simple authentication:

```python
import streamlit as st

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.form("login"):
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if password == "your-password":  # Hard-coded for demo
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Wrong password")
else:
    # Rest of app here
    st.write("Welcome!")
```

**For production**: Use proper auth library like `streamlit-authenticator`.

---

## 🐛 Troubleshooting Guide

### Issue: Port 8501 already in use

**Symptoms**: 
```
Error: Address already in use
```

**Solutions**:
```bash
# Use different port
streamlit run main.py --server.port 8502

# Or kill process using port 8501
lsof -i :8501  # Find process
kill -9 <PID>  # Kill it
```

---

### Issue: "streamlit: command not found"

**Symptoms**:
```
bash: streamlit: command not found
```

**Solutions**:
```bash
# 1. Install streamlit
pip install streamlit

# 2. Verify installation
pip list | grep streamlit

# 3. Use full path
python -m streamlit run main.py
```

---

### Issue: ImportError: No module named 'google'

**Symptoms**:
```
ModuleNotFoundError: No module named 'google'
```

**Solutions**:
```bash
# Install Gemini API
pip install google-generativeai

# Or install all requirements
pip install -r requirements.txt
```

---

### Issue: API returns "403 Forbidden"

**Symptoms**:
```
Error: 403 Forbidden from API
```

**Causes & Solutions**:
```python
# 1. Check API key is correct
# Edit .env, verify GEMINI_API_KEY value

# 2. Check API key has permissions
# Visit: console.cloud.google.com

# 3. Verify URL is correct
# Should be: https://aistudio.google.com

# 4. Wait for key to activate
# New keys take 1-2 minutes
```

---

### Issue: Memory usage keeps growing

**Symptoms**:
```
App gets slower over time
Memory usage: 500+ MB
```

**Solutions**:
```python
# 1. Add caching with TTL
@st.cache_data(ttl=3600)  # 1 hour
def get_data():
    return api.call()

# 2. Limit history
if len(chat_history) > 100:
    chat_history = chat_history[-50:]

# 3. Clear cache periodically
# Restart app daily with: systemctl restart streamlit

# 4. Disable stats
# In .streamlit/config.toml:
[client]
gatherUsageStats = false
```

---

### Issue: "st.set_page_config() called twice"

**Symptoms**:
```
Error: st.set_page_config() already called once
```

**Cause**: Multiple `st.set_page_config()` calls

**Solution**:
```python
# Only call ONCE in main.py, NEVER in feature modules
# Wrong:
# pages/feature.py
st.set_page_config(...)  # ❌ Wrong!

# Right:
# main.py
st.set_page_config(...)  # ✅ Correct!

# pages/feature.py
def run_feature():
    # No st.set_page_config() here
    st.write("...")
```

---

### Issue: Can't connect to database

**Symptoms**:
```
Error: could not connect to server: No such file or directory
```

**Solutions**:
```python
# 1. Check database is running
# PostgreSQL: sudo systemctl start postgresql
# SQLite: N/A (file-based)

# 2. Check connection string
# Should be: postgresql://user:pass@localhost:5432/dbname

# 3. Check credentials
# Verify: username, password, host, port

# 4. Check firewall
# Allow port 5432 for PostgreSQL
```

---

### Issue: Image upload fails

**Symptoms**:
```
Error uploading file / File too large
```

**Solutions**:
```python
# 1. Check file size limit
# Default: 200MB
# Edit in .streamlit/config.toml:
[server]
maxUploadSize = 500  # Increase to 500MB

# 2. Compress image first
from PIL import Image
img = Image.open("path.jpg")
img.thumbnail((1000, 1000))  # Resize
img.save("compressed.jpg")
```

---

### Issue: Sidebar buttons don't work

**Symptoms**:
```
Click button → Nothing happens
```

**Solutions**:
```python
# 1. Check session state initialization
if "page" not in st.session_state:
    st.session_state.page = "Home"

# 2. Trigger rerun after state change
st.session_state.page = "New_Page"
st.rerun()

# 3. Use st.session_state for persistence
# Not just local variables

# 4. Check button callback
if st.button("Label"):
    st.session_state.page = "Label_Analyzer"
    st.rerun()
```

---

### Issue: Chat history disappears after reload

**Symptoms**:
```
Refresh page → Chat history gone
```

**Solution**: Use session state!

```python
# Right way:
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.session_state.chat_history.append(msg)

# Wrong way: ❌
chat_history = []  # Lost on reload!
chat_history.append(msg)
```

---

### Issue: Slow performance / API rate limiting

**Symptoms**:
```
App is slow
API returns 429 (too many requests)
```

**Solutions**:
```python
# 1. Add caching
@st.cache_data(ttl=3600)
def expensive_function():
    return result

# 2. Add request throttling
import time
time.sleep(1)  # Wait 1 second between requests

# 3. Check API rate limits
# Gemini: free tier has limits
# Upgrade if needed

# 4. Batch requests
# Make fewer requests, process more data per request
```

---

### Issue: .env file not being loaded

**Symptoms**:
```
Error: API key not found
```

**Solutions**:
```bash
# 1. Check .env exists in project root
ls -a | grep .env

# 2. Check format is correct
# Should be: VARIABLE_NAME=value
# Not: VARIABLE_NAME = value (no spaces!)

# 3. Restart app
# Changes don't take effect until restart

# 4. Use explicit loading
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
```

---

### Issue: GitHub deployment fails

**Symptoms**:
```
Build failed on Streamlit Cloud
```

**Solutions**:
1. Check requirements.txt has all packages
2. Verify secrets are added in Settings
3. Check main.py exists in repository root
4. Review deployment logs in Streamlit Cloud

---

## ✨ Quick Tips & Tricks

### Tip 1: Speed up development
```bash
# Run with reload enabled (auto-reload on save)
streamlit run main.py --logger.level=debug
```

### Tip 2: Debug print statements
```python
import streamlit as st

# Use expander to hide debug info
with st.expander("🐛 Debug Info"):
    st.write(st.session_state)
    st.write(my_variable)
```

### Tip 3: Test offline
```bash
# Works without internet if data is cached!
streamlit run main.py --client.gatherUsageStats=false
```

### Tip 4: Optimize images
```python
from PIL import Image
img = Image.open("large.jpg")
img.thumbnail((800, 800), Image.Resampling.LANCZOS)
img.save("optimized.jpg")
```

### Tip 5: Monitor memory
```bash
# On Linux/Mac
ps aux | grep streamlit

# On Windows
tasklist | findstr streamlit
```

---

## 📚 More Resources

- **Official Docs**: https://docs.streamlit.io
- **Streamlit Forum**: https://discuss.streamlit.io
- **GitHub Issues**: https://github.com/streamlit/streamlit/issues
- **API Reference**: https://docs.streamlit.io/library/api-reference

---

## 🆘 Still Stuck?

1. **Check the docs**: [ARCHITECTURE.md](ARCHITECTURE.md)
2. **Search Google**: "streamlit [your error]"
3. **Ask on forum**: https://discuss.streamlit.io
4. **Read error message carefully**: Often has hints!

---

**Last Updated**: February 11, 2026  
**Status**: ✅ Complete

---

### Quick Navigation
- [📓 Main Docs](QUICKSTART.md)
- [🏗️ Architecture](ARCHITECTURE.md)
- [🚀 Deployment](DEPLOYMENT.md)
- [📑 File Index](INDEX.md)

---

**You're not alone!** Most issues have been solved before. Use this guide and you'll find the answer. 💪
