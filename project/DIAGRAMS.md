# Architecture Diagrams - Label Padega Sabh

## 1. Application Flow

```
User Browser
    ↓
    ├─→ [http://localhost:8501]
    │
    └─→ main.py (Streamlit App)
        ├─ Set Page Config (once)
        ├─ Sidebar Navigation
        └─ Session State Manager
            ├─ Store current page
            ├─ Store chat history
            ├─ Store analysis data
            └─ Store user preferences
```

---

## 2. Navigation Structure

```
┌─────────────────────────────────────────┐
│           Label Padega Sabh              │
│        Sidebar Navigation (Always)      │
├─────────────────────────────────────────┤
│ 🍎 Home              ←─────────────────┐ │
│ 📊 Label Analyzer         [Current]    │ │
│ 📱 Barcode Scanner        Page Region  │ │
│ 💬 Nutrition Chatbot      (Cached)     │ │
│ 💊 Medicine Checker                    │ │
│ ℹ️ About            ←─────────────────┐ │
│ 📋 Guidelines                         │ │
│ 📞 Helplines        ←─────────────────┘ │
└─────────────────────────────────────────┘
```

---

## 3. Module Dependency Graph

```
                        main.py
                    (Entry Point)
                          ↓
                ┌─────────┼─────────┐
                ↓         ↓         ↓
         Sidebar Setup  Session   Page Routing
                        State
                          ↓
        ┌─────────────────┼──────────────────┐
        ↓                 ↓                  ↓
    [Static Pages]   [Dynamic Pages]   [Utilities]
    ├─ Home          ├─ Label Analyzer  ├─ styles.py
    ├─ About         ├─ Barcode         ├─ cache
    ├─ Guidelines    ├─ Chatbot         └─ config
    └─ Helplines     └─ Medicines
            ↓              ↓              ↓
        Markdown      Streamlit        External
        + HTML       Components      APIs (Gemini)
```

---

## 4. Data Flow

```
User Input
    ↓
Streamlit Widget
    ↓
Session State Update
    ↓
Feature Module
    ├─ Process data
    ├─ Call API
    └─ Format output
        ↓
    Display Result
        ↓
    Cache for performance
```

---

## 5. Session State Management

```
st.session_state
├── page: str = "Home"              # Current page
├── chat_history: list = []         # Chat messages
├── product_data: dict = {}         # Product info
├── analysis_data: dict = {}        # Analysis results
├── user_preferences: dict = {}     # User settings
└── scan_history: list = []         # Previous scans
```

---

## 6. Feature Module Pattern

```
pages/feature.py
├─ Imports
├─ Configuration
├── Helper Functions
│   ├─ validate_input()
│   ├─ process_data()
│   └─ format_output()
├── Main Function (UI)
│   ├─ Display header
│   ├─ Get user input
│   ├─ Call helpers
│   └─ Show results
└─ Entry Point
    └─ run_feature_name():
        └─ main()   # Called from main.py
```

---

## 7. API Integration

```
User Input (main.py)
    ↓
Feature Module
    ├─ Label Analyzer  → Google Gemini API
    │                    └─ Image Analysis
    │
    ├─ Barcode Scanner → Open Food Facts API
    │                    └─ Product Database
    │
    ├─ Chatbot        → Google Gemini API
    │                    └─ Language Generation
    │
    └─ Medicine       → Google Gemini API
                        └─ Medicine Analysis

Cache Layer (Optional)
  ↓
Display Results
```

---

## 8. File Organization

```
project/
│
├── main.py ⭐                    [Entry Point]
│   ├─ Page config (once)
│   ├─ Global styles
│   ├─ Sidebar nav
│   ├─ Page routing
│   └─ Static pages
│
├── pages/                        [Features]
│   ├─ finalanalyzerbot.py
│   │   └─ run_label_analyzer()
│   ├─ barcode.py
│   │   └─ run_barcode_scanner()
│   ├─ chatbot.py
│   │   └─ run_nutrition_chatbot()
│   ├─ medicines.py
│   │   └─ run_medicine_analyzer()
│   └─ __init__.py
│
├── utils/                        [Helpers]
│   ├─ styles.py                 [CSS]
│   └─ __init__.py
│
├── .streamlit/                   [Config]
│   ├─ config.toml
│   └─ secrets.toml (git ignored)
│
├── static/
│   └─ images/                   [Assets]
│
├── requirements.txt             [Dependencies]
├── .env                         [Secrets]
├── .gitignore
└── Documentation (*.md files)
```

---

## 9. Deployment Architecture

```
Local Development
├─ main.py
├─ .env (with real keys)
└─ Run: streamlit run main.py

         ↓↓↓ Push to GitHub ↓↓↓

Cloud Deployment (Streamlit Cloud)
├─ main.py
├─ requirements.txt
├─ .streamlit/config.toml
└─ .streamlit/secrets.toml
    └─ Public URL: app.streamlit.app
```

---

## 10. State Lifecycle

```
App Starts
  ↓
Initialize Session State
  ├─ page = "Home"
  ├─ chat_history = []
  ├─ product_data = {}
  └─ Other state vars
  ↓
User Interaction
  ├─ Click sidebar button
  ├─ Update st.session_state.page
  └─ Trigger rerun (automatic)
  ↓
Render New Page
  ├─ Run if st.session_state.page == "Label_Analyzer":
  │   └─ run_label_analyzer()
  └─ Display page with cached state
  ↓
User Interaction Again
  └─ goto: User Interaction (loop)
  ↓
Browser Closed
  └─ Session cleared (all state lost)
```

---

## 11. Error Handling Flow

```
User Action
  ↓
Try to Execute
  ├─ Success
  │   └─ Display Result
  │
  └─ Error
      ├─ Catch Exception
      ├─ Log Error
      ├─ Sanitize Message
      └─ Show User-Friendly Error
          ├─ st.error("❌ Error message")
          └─ st.info("💡 Suggestion")
```

---

## 12. Performance Optimization

```
Without Caching
API Request → Process → Display → (repeat every time)
    ✅ Always fresh
    ❌ Slow, rate limited

With Caching (Recommended)
API Request → Cache Check → Use Cache/New Result → Display
    ✅ Fast (from cache)
    ✅ Fewer API calls
    ❌ May show old data

Implementation:
@st.cache_data(ttl=3600)  # Cache for 1 hour
def expensive_function():
    return api.call()
```

---

## 13. Security Architecture

```
Secrets Management
├─ Local Dev: .env file (git ignored)
├─ Cloud: .streamlit/secrets.toml (not committed)
└─ Both contain API keys
    └─ Accessed via: st.secrets["key_name"]

Session Isolation
├─ Each user gets separate session
├─ Data not shared between users
└─ Session cleared on browser close

HTTPS
├─ Local: HTTP (dev only)
└─ Cloud: HTTPS (automatic, Streamlit Cloud)
```

---

## 14. Comparison: Old vs New

### OLD (Flask + Subprocess)
```
Browser:5000  ← Flask Server
  ├─ Route: / → render_template()
  ├─ Route: /analyze → exec subprocess
  │   └─ Browser:8501 ← New Streamlit Process
  │       ├─ Port conflict risk
  │       ├─ Memory: 500+ MB
  │       ├─ Startup: 8-10s
  │       └─ State lost
```

### NEW (Streamlit Unified)
```
Browser:8501  ← Streamlit App
  ├─ Page: Home (sidebar)
  ├─ Page: Label Analyzer (sidebar)
  ├─ Page: Chatbot (sidebar)
  └─ All in single process
      ├─ No conflicts
      ├─ Memory: 150-200 MB
      ├─ Startup: 2-3s
      └─ State shared
```

---

## 15. Scaling Strategy

### Current (Single Instance)
```
Users (1-100)
    ↓
    └─→ Single main.py
        └─ Streamlit Server
            └─ Works for dev/small teams
```

### Future (Production Scale)
```
Users (100-10,000)
    ↓
Load Balancer
    ├─→ Server 1: main.py
    ├─→ Server 2: main.py
    ├─→ Server 3: main.py
    └─→ Server N: main.py
        ↓
    Shared Database
    Shared Cache (Redis)
    CDN for static files
```

---

## Quick Reference

### Page Navigation Pattern
```python
# In main.py
with st.sidebar:
    if st.button("📊 Label Analyzer"):
        st.session_state.page = "Label_Analyzer"

# Later in main
if st.session_state.page == "Label_Analyzer":
    from pages.finalanalyzerbot import run_label_analyzer
    run_label_analyzer()
```

### Session State Pattern
```python
# Initialize
if "my_data" not in st.session_state:
    st.session_state.my_data = []

# Use
st.session_state.my_data.append(new_item)

# Access
data = st.session_state.my_data
```

### Caching Pattern
```python
@st.cache_data(ttl=3600)  # 1 hour TTL
def expensive_function(param):
    # This runs only once per param
    return result

result = expensive_function("value")
```

---

## Troubleshooting Using These Diagrams

### "Page won't load"
→ Check: Navigation Structure (#2) + Error Handling (#11)

### "Session data lost"
→ Check: State Lifecycle (#10) + Session Management (#13)

### "API calls too slow"
→ Check: API Integration (#7) + Performance (#12)

### "Secrets not working"
→ Check: Security Architecture (#13) + File Organization (#8)

### "Memory usage high"
→ Check: Scaling Strategy (#15) + Performance (#12)

---

## Connection Map

```
        main.py
        (Center)
         / | \
        /  |  \
    Pages Utils Config
      |    |    |
    [Feature] [Style] [.env]
     Code    CSS     Secrets
      |
    [API]
    (Gemini)
```

---

**Visual Guide Created**: February 11, 2026
**Status**: Complete and Ready for Reference
