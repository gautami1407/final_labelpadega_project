# Label Padega Sabh - Streamlit Conversion Guide

## 🎯 Project Overview

This document provides a complete guide to the newly converted Streamlit application. The application has been completely redesigned from a Flask multi-process architecture to a unified Streamlit single-page application (SPA).

---

## 📁 Recommended Folder Structure

```
project/
├── main.py                          # ⭐ Main Streamlit entry point
├── requirements.txt                 # Python dependencies
├── .streamlit/
│   ├── config.toml                 # Streamlit configuration
│   └── secrets.toml                # (Optional) API keys for deployment
├── pages/
│   ├── __init__.py                 # Make it a Python package
│   ├── finalanalyzerbot.py         # Food Label Analyzer
│   ├── barcode.py                  # Barcode Scanner
│   ├── chatbot.py                  # Nutrition Chatbot
│   └── medicines.py                # Medicine Safety Checker
├── static/
│   ├── images/                     # Store static images here
│   ├── logos/
│   └── icons/
├── utils/                          # (Optional) Utility functions
│   ├── __init__.py
│   ├── helpers.py                  # Helper functions
│   └── config.py                   # Configuration constants
├── .gitignore
├── README.md
└── .env                            # (Optional) Local environment variables
```

---

## 🚀 Quick Start

### 1. **Installation**

```bash
# Navigate to project directory
cd project

# Install dependencies
pip install -r requirements.txt

# On Windows, install pytesseract dependency (optional, for medicine scanning)
# Download Tesseract-OCR: https://github.com/UB-Mannheim/tesseract/wiki
```

### 2. **Configuration**

Create a `.env` file in the project root for sensitive information:

```env
# .env
GEMINI_API_KEY=your_api_key_here
USDA_API_KEY=your_usda_key_here
```

Or, for Streamlit Cloud deployment, use `.streamlit/secrets.toml`:

```toml
# .streamlit/secrets.toml
gemini_api_key = "your_api_key_here"
usda_api_key = "your_usda_key_here"
```

### 3. **Run Locally**

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`

---

## 📋 Environment Variables

The app uses the following environment variables (you can set them in `.env` or `.streamlit/secrets.toml`):

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API Key | Yes |
| `USDA_API_KEY` | USDA Food Database API Key | No |

### Important Security Notes:
- **Never commit `.env` or `secrets.toml` to Git**
- Add them to `.gitignore`
- They are automatically loaded by Streamlit in production

---

## 🏗️ Architecture Overview

### Old Architecture (Flask-based)
```
Flask App
├── Route: /
├── Route: /about
├── Route: /guidelines
├── Route: /helplines
├── Route: /start-scanning    → subprocess → finalanalyzerbot.py
├── Route: /start-barcode     → subprocess → barcode.py
├── Route: /start-chatbot     → subprocess → chatbot.py
└── Route: /start-medicine    → subprocess → medicines.py
```

### New Architecture (Streamlit-based)
```
main.py (Single Streamlit App)
├── Sidebar Navigation
├── Session State Management
└── Page Routing:
    ├── Home          (main.py)
    ├── Label Analyzer (finalanalyzerbot.py)
    ├── Barcode Scanner (barcode.py)
    ├── Chatbot       (chatbot.py)
    ├── Medicine      (medicines.py)
    ├── About         (main.py)
    ├── Guidelines    (main.py)
    └── Helplines     (main.py)
```

**Key Benefits:**
- ✅ No subprocess overhead
- ✅ Shared session state across modules
- ✅ Better performance
- ✅ Single deployment unit
- ✅ Cleaner URL structure
- ✅ Enhanced user experience

---

## 🔧 Module Structure

### `main.py` (Main Entry Point)

Entry point for the entire application. Contains:

- **Global Configuration**: `st.set_page_config()`
- **Custom Styling**: CSS with theme colors
- **Sidebar Navigation**: Options for all features
- **Page Routing**: Logic to display selected page
- **Static Pages**: Home, About, Guidelines, Helplines

```python
# Navigation structure
nav_options = {
    "🏠 Home": "Home",
    "📊 Label Analyzer": "Label_Analyzer",
    "📱 Barcode Scanner": "Barcode_Scanner",
    "💬 Nutrition Chatbot": "Chatbot",
    "💊 Medicine Checker": "Medicine_Checker",
    "ℹ️ About": "About",
    "📋 Guidelines": "Guidelines",
    "📞 Helplines": "Helplines"
}
```

### `pages/finalanalyzerbot.py` (Food Label Analyzer)

**Function to import**: `run_label_analyzer()`

Features:
- Upload food package images
- AI-powered nutritional analysis
- Health rating (1-10 scale)
- Ingredient breakdown
- Allergen information
- Custom report generation

**Modified for module import**:
- Removed `st.set_page_config()` from the function
- Wrapped UI in `render_main_ui()` method
- Exposed `run_label_analyzer()` function

### `pages/barcode.py` (Barcode Scanner)

**Function to import**: `run_barcode_scanner()`

Features:
- Scan product barcodes
- Search products by name
- Health & safety analysis
- Regulatory compliance checks
- Allergen alerts
- Product recalls database
- Environmental impact assessment

**Modified for module import**:
- Removed `st.set_page_config()`
- Added `run_barcode_scanner()` function
- Uses local caching for offline functionality

### `pages/chatbot.py` (Nutrition Chatbot)

**Function to import**: `run_nutrition_chatbot()`

Features:
- AI-powered nutrition advice
- Food image analysis
- Personalized diet suggestions
- Health statistics dashboard
- Chat history
- Suggested questions

**Modified for module import**:
- Removed `st.set_page_config()`
- Added `render_main_ui()` method
- Added `run_nutrition_chatbot()` function

### `pages/medicines.py` (Medicine Safety Checker)

**Function to import**: `run_medicine_analyzer()`

Features:
- Upload medicine labels
- Check drug interactions
- Side effects database
- Medical conditions screening
- OCR-based text extraction
- Medicine chatbot

**Modified for module import**:
- Removed `st.set_page_config()`
- Added `render_main_ui()` function
- Added `run_medicine_analyzer()` function

---

## 📝 Session State Management

The application uses Streamlit's session state to maintain data across interactions:

```python
# Initialize in main.py or individual modules
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "product_data" not in st.session_state:
    st.session_state.product_data = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
```

---

## 🎨 Custom Styling

The app uses custom CSS defined in `main.py` for consistent theming:

**Primary Color**: `#059669` (Emerald Green)
**Secondary**: `#027353` (Dark Green)
**Accent**: `#38a169` (Fresh Green)

### Default Card Styles:
- `.feature-card` - Feature information cards
- `.stat-box` - Statistics display
- `.highlight` - Highlighted text
- `.success-box` - Success messages
- `.warning-box` - Warning messages
- `.danger-box` - Danger/error messages

---

## 🚢 Deployment

### **Streamlit Cloud** (Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Convert to Streamlit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [streamlit.io/cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Select your repository and `main.py`
   - Add secrets in "Advanced Settings"

3. **Set Secrets**:
   - In Streamlit Cloud > Settings > Secrets
   - Add `GEMINI_API_KEY` and `USDA_API_KEY`

### **Other Platforms** (Docker, Heroku, AWS)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Run with Docker:
```bash
docker build -t label-padega .
docker run -p 8501:8501 label-padega
```

---

## 📚 API Keys & Configuration

### Google Gemini API

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Add to `.env` or `.streamlit/secrets.toml`:
   ```
   GEMINI_API_KEY=sk-xxxxx
   ```

### USDA Food Database API

1. Register at [USDA FDC API](https://fdc.nal.usda.gov/api-key-signup.html)
2. Add to `.env` or `.streamlit/secrets.toml`:
   ```
   USDA_API_KEY=xxxxx
   ```

---

## 🔄 Modifying the App

### Adding a New Feature Page

1. Create a new file in `pages/`:
   ```python
   # pages/myfeature.py
   import streamlit as st
   
   def run_my_feature():
       st.markdown("### 🎯 My Feature")
       st.write("Feature content here...")
   ```

2. Add navigation to `main.py`:
   ```python
   nav_options = {
       # ... existing items ...
       "🎯 My Feature": "My_Feature",
   }
   ```

3. Add page routing in `main.py`:
   ```python
   elif st.session_state.page == "My_Feature":
       try:
           from pages.myfeature import run_my_feature
           run_my_feature()
       except Exception as e:
           st.error(f"Error loading My Feature: {str(e)}")
   ```

### Customizing Styles

Edit the CSS in `main.py` under the `st.markdown()` section:

```python
st.markdown("""
<style>
    .my-custom-style {
        background-color: #your-color;
        padding: 20px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)
```

---

## 🐛 Troubleshooting

### Issue: Modules not found
**Solution**: Ensure `pages/` is a Python package:
```bash
touch pages/__init__.py
```

### Issue: Page config called twice
**Solution**: Removed all `st.set_page_config()` from feature modules. Only `main.py` calls it.

### Issue: API key errors
**Solution**: 
- Verify keys in `secrets.toml` (production) or `.env` (local)
- Check in terminal: `echo $GEMINI_API_KEY`

### Issue: Slow performance
**Solution**: 
- Use caching: `@st.cache_data`
- Disable `gatherUsageStats` in `config.toml`

---

## ✅ Testing Checklist Before Deployment

- [ ] All navigation buttons work
- [ ] Page transitions don't crash
- [ ] API keys are correctly loaded
- [ ] Images display properly
- [ ] Chat history persists in session
- [ ] File uploads work
- [ ] No console errors
- [ ] Responsive on mobile
- [ ] All links work
- [ ] Settings persist in sidebar

---

## 📞 Support & Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Google Gemini Docs**: https://ai.google.dev/docs
- **USDA FDC API**: https://fdc.nal.usda.gov/api-docs
- **Community**: https://discuss.streamlit.io

---

## 📄 File Reference

### Main Files

| File | Purpose |
|------|---------|
| `main.py` | Application entry point & routing |
| `requirements.txt` | Python dependencies |
| `.env` | Local environment variables |
| `.streamlit/config.toml` | Streamlit configuration |
| `.streamlit/secrets.toml` | Production secrets (not in Git) |

### Feature Modules

| File | Feature |
|------|---------|
| `pages/finalanalyzerbot.py` | Food Label Analysis |
| `pages/barcode.py` | Barcode Scanning |
| `pages/chatbot.py` | Nutrition Chatbot |
| `pages/medicines.py` | Medicine Safety |

### Static Assets

| Directory | Content |
|-----------|---------|
| `static/images/` | App images & logos |
| `utils/` | Helper functions & utilities |

---

## 🎉 Next Steps

1. ✅ Test locally with `streamlit run main.py`
2. ✅ Deploy to Streamlit Cloud
3. ✅ Set up CI/CD for automatic deployments
4. ✅ Monitor app performance
5. ✅ Gather user feedback and iterate

---

## 📝 Version History

- **v1.0** (Current): Complete conversion from Flask to Streamlit
  - Unified single-page application
  - Removed subprocess overhead
  - Enhanced user interface
  - Better session management
  - Cloud-ready deployment

**Previous**: Flask multi-process architecture (deprecated)

---

**Last Updated**: February 11, 2026
**Status**: ✅ Production Ready
**License**: [Your License Here]
