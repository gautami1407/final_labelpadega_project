# 🍎 Label Padega Sabh - Your Food Detective

A comprehensive Streamlit application for food label analysis, barcode scanning, nutrition guidance, and medicine safety checking using AI.

## ✨ Features

### 📊 **Food Label Analyzer**
- Upload food package images
- AI-powered nutritional analysis using Google Gemini
- Comprehensive health scoring (1-10 scale)
- Ingredient breakdown with health impact
- Allergen detection
- Processing level classification
- Custom report generation

### 📱 **Barcode Scanner**
- Real-time barcode scanning
- Product lookup via multiple databases
- Regulatory compliance checking
- Safety certifications verification
- Banned ingredients detection
- Product recall alerts
- Environmental impact assessment
- Healthier alternatives suggestions

### 💬 **Nutrition Chatbot**
- AI-powered nutrition advice
- Food image analysis and recommendations
- Personalized diet suggestions
- Health statistics tracking
- Conversational interface
- Suggested questions for guidance

### 💊 **Medicine Safety Checker**
- Medicine label analysis
- Drug interaction checking
- Side effects database
- Medical condition screening
- OCR-based text extraction
- Educational information

### 📚 **Additional Resources**
- Food health guidelines
- Government helplines
- Health tips and facts
- Regulatory information
- FAQ and support

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Google Gemini API Key ([Get it free](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone/Download the project**
   ```bash
   cd project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_api_key_here
   USDA_API_KEY=your_usda_key_here  # Optional
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open in browser**
   ```
   http://localhost:8501
   ```

---

## 📁 Project Structure

```
project/
├── main.py                     # Main application entry point
├── requirements.txt            # Python dependencies
├── .env                       # Environment variables (not in Git)
├── .streamlit/
│   └── config.toml           # Streamlit configuration
├── pages/
│   ├── finalanalyzerbot.py   # Food Label Analyzer
│   ├── barcode.py            # Barcode Scanner
│   ├── chatbot.py            # Nutrition Chatbot
│   └── medicines.py          # Medicine Checker
├── static/images/            # Static assets
├── ARCHITECTURE.md           # Detailed documentation
└── README.md                 # This file
```

---

## 🎯 Usage

### Food Label Analyzer
1. Click **"📊 Label Analyzer"** from the sidebar
2. Upload an image of a food package
3. Wait for AI analysis
4. Review nutritional information and health scores
5. Download detailed reports

### Barcode Scanner
1. Click **"📱 Barcode Scanner"** from the sidebar
2. Enter a barcode number or product name
3. View comprehensive product information
4. Check for safety alerts and alternatives

### Chat with Nutritionist
1. Click **"💬 Nutrition Chatbot"** from the sidebar
2. Ask questions about nutrition
3. Upload food images for analysis
4. Get personalized diet recommendations

### Medicine Safety Check
1. Click **"💊 Medicine Checker"** from the sidebar
2. Upload a medicine package image
3. Review safety information and interactions
4. Check for your medical conditions

---

## 🔧 Configuration

### Environment Variables

Required:
- `GEMINI_API_KEY` - Google Gemini API Key

Optional:
- `USDA_API_KEY` - USDA Food Database API Key

### Streamlit Configuration

Edit `.streamlit/config.toml` to customize:
- Theme colors
- Page layout
- Cache settings
- Server options

---

## 🚢 Deployment

### **Streamlit Cloud** (Recommended)

1. Push code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create new app from repository
4. Add secrets in "Advanced Settings"

### **Docker**

```bash
docker build -t label-padega .
docker run -p 8501:8501 label-padega
```

### **Other Platforms**

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed deployment guides.

---

## 📊 Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.11+
- **AI/ML**: Google Gemini API
- **Data**: Open Food Facts, USDA FDC API
- **Visualization**: Plotly
- **Image Processing**: Pillow, pytesseract

---

## 🔒 Security & Privacy

- ✅ No data stored permanently
- ✅ API keys kept in environment variables
- ✅ CORS enabled for security
- ✅ HTTPS ready for deployment
- ✅ User data not logged

---

## 📝 Development

### Creating New Features

1. Create a new module in `pages/`
2. Export a `run_feature()` function
3. Add to navigation in `main.py`
4. Add page routing logic

### Testing Locally

```bash
# Run with cache disabled
streamlit run main.py --logger.level=debug

# Run with specific config
streamlit run main.py --config.headless=true
```

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
touch pages/__init__.py
```

### API Key not working
- Verify key in `.env` or `.streamlit/secrets.toml`
- Check key has necessary permissions
- Try generating a new key

### Slow performance
- Enable caching: Clear `.streamlit/cache` folder
- Disable `gatherUsageStats` in config.toml
- Use `@st.cache_data` decorator

### Image upload fails
- Check file size (< 200MB)
- Verify format (JPG, PNG)
- Check disk space

---

## 📞 Support

- 📖 **Documentation**: See [ARCHITECTURE.md](ARCHITECTURE.md)
- 🐛 **Bug Reports**: Create an issue
- 💡 **Feature Requests**: Discuss in issues
- 🎓 **Learning**: Check Streamlit docs

---

## 📜 License

[Your License Here]

---

## 👥 Contributors

- **Your Name** - Project Lead
- **Team Members** - Development

---

## 📈 Roadmap

- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Offline mode
- [ ] Advanced analytics dashboard
- [ ] Meal planning integration
- [ ] Recipe suggestions
- [ ] Community features

---

## 🙏 Acknowledgments

- Google for Gemini API
- Open Food Facts community
- USDA for Food Data Central
- Streamlit team for the framework

---

**Version**: 1.0  
**Status**: ✅ Production Ready  
**Last Updated**: February 11, 2026

---

### 🚀 Ready to Get Started?

```bash
pip install -r requirements.txt
streamlit run main.py
```

Enjoy your journey to healthier eating! 🍎
