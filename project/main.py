"""
Label Padega Sabh - All-in-One Food & Medicine Analysis Platform
A unified Streamlit application for food label analysis, barcode scanning, 
nutrition chatbot, and medicine safety checking.
"""

import streamlit as st
from pathlib import Path
import sys

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Label Padega Sabh - Your Food Detective",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Label Padega Sabh v1.0 - Food & Medicine Analysis Platform"
    }
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================
st.markdown("""
<style>
    /* Main theme styling */
    :root {
        --primary-color: #059669;
        --secondary-color: #027353;
        --accent-color: #38a169;
    }
    
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #2E7D32;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .feature-card {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #059669;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        box-shadow: 0 4px 12px rgba(5, 150, 105, 0.2);
        transform: translateX(5px);
    }
    
    .stat-box {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #a7f3d0;
    }
    
    .highlight {
        background-color: #fef3c7;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
with st.sidebar:
    st.title("🍎 Label Padega Sabh")
    st.markdown("---")
    
    # Navigation buttons
    st.markdown("<h3 style='color: #059669;'>Navigation</h3>", unsafe_allow_html=True)
    
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
    
    for label, page in nav_options.items():
        if st.button(label, use_container_width=True, 
                     key=f"nav_{page}",
                     help=f"Go to {label}"):
            st.session_state.page = page
            st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div class='stat-box'>
        <p style='font-size: 12px; margin: 0;'><strong>Version:</strong> 1.0</p>
        <p style='font-size: 12px; margin: 5px 0 0 0;'><strong>Status:</strong> ✅ Active</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: HOME
# ============================================================================
def page_home():
    st.markdown("<h1 style='text-align: center; color: #059669;'>🍎 Label Padega Sabh</h1>", 
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #666;'>Your Food Detective - Know What You Eat</h3>", 
                unsafe_allow_html=True)
    
    # News ticker
    st.markdown("""
    <div style='background: linear-gradient(135deg, #059669, #027353); color: white; padding: 15px; 
                border-radius: 8px; margin: 20px 0; font-size: 14px;'>
        <strong>📰 Health Tips:</strong> 60% of our diet should consist of fresh fruits and vegetables! | 
        Always check for added sugars when buying packaged foods | 
        The recommended daily intake of water is 8 glasses to stay hydrated
    </div>
    """, unsafe_allow_html=True)
    
    # Features overview
    st.markdown("<h2 style='color: #059669;'>✨ Our Features</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h4>📊 Label Analyzer</h4>
            <p>Upload food package images and get instant nutritional analysis powered by AI. 
            Understand ingredients, nutritional values, and health impact.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
            <h4>📱 Barcode Scanner</h4>
            <p>Scan product barcodes or upload images. Get comprehensive product information including 
            health ratings, harmful ingredients, and safety certifications.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h4>💬 Nutrition Chatbot</h4>
            <p>Ask questions about nutrition, diet plans, and food health. Get personalized advice 
            from our AI-powered nutrition assistant.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
            <h4>💊 Medicine Checker</h4>
            <p>Upload medicine labels or packages. Check for drug interactions, side effects, 
            and safety information for your medical conditions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown("<h2 style='color: #059669;'>📈 Why Choose Us?</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='stat-box'>
            <h3>✅</h3>
            <p><strong>AI-Powered</strong><br>Gemini AI Analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='stat-box'>
            <h3>🚀</h3>
            <p><strong>Instant Results</strong><br>Real-time Processing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='stat-box'>
            <h3>📊</h3>
            <p><strong>Detailed Reports</strong><br>Comprehensive Analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='stat-box'>
            <h3>🛡️</h3>
            <p><strong>Safe & Secure</strong><br>Your Privacy Protected</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; padding: 20px; background: #ecfdf5; border-radius: 8px; border-left: 4px solid #059669;'>
        <h3 style='color: #059669; margin: 0;'>🎯 Get Started Today!</h3>
        <p style='margin: 10px 0; color: #666;'>Choose any feature from the sidebar to begin your food and health analysis journey.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: LABEL ANALYZER
# ============================================================================
def page_label_analyzer():
    st.markdown("<h1 style='color: #059669;'>📊 Food Label Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("Upload a food package image and get instant AI-powered nutritional analysis")
    
    try:
        # Import the label analyzer module
        from pages.finalanalyzerbot import run_label_analyzer
        run_label_analyzer()
    except Exception as e:
        st.error(f"❌ Error loading Label Analyzer: {str(e)}")
        st.info("Make sure the `pages/finalanalyzerbot.py` is properly configured.")

# ================================================
# ===============================================
def page_barcode_scanner():
    st.markdown("<h1 style='color: #059669;'>📱 Barcode Scanner & Product Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("Scan product barcodes or upload images to get comprehensive product information")
    
    try:
        # Import the barcode scanner module
        from pages.barcode import run_barcode_scanner
        run_barcode_scanner()
    except Exception as e:
        st.error(f"❌ Error loading Barcode Scanner: {str(e)}")
        st.info("Make sure the `pages/barcode.py` is properly configured.")

# ============================================================================
# PAGE: CHATBOT
# ============================================================================
def page_chatbot():
    st.markdown("<h1 style='color: #059669;'>💬 Nutrition Chatbot</h1>", unsafe_allow_html=True)
    st.markdown("Ask questions about nutrition, diet, and food health. Upload images for food analysis.")
    
    try:
        # Import the chatbot module
        from pages.chatbot import run_nutrition_chatbot
        run_nutrition_chatbot()
    except Exception as e:
        st.error(f"❌ Error loading Chatbot: {str(e)}")
        st.info("Make sure the `pages/chatbot.py` is properly configured.")


# PAGE: MEDICINE CHECKER
# ============================================================================
def page_medicine_checker():
    st.markdown("<h1 style='color: #059669;'>💊 Medicine Safety Checker</h1>", unsafe_allow_html=True)
    st.markdown("Upload medicine labels to check for interactions, side effects, and safety information")
    
    try:
        # Import the medicine checker module
        from pages.medicines import run_medicine_analyzer
        run_medicine_analyzer()
    except Exception as e:
        st.error(f"❌ Error loading Medicine Checker: {str(e)}")
        st.info("Make sure the `pages/medicines.py` is properly configured.")


# PAGE: ABOUT
# ============================================================================
def page_about():
    st.markdown("<h1 style='color: #059669;'>ℹ️ About Us</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>Mission</h3>
        <p>Label Padega Sabh aims to empower individuals to make informed decisions about their food 
        and medicine consumption by providing AI-powered analysis of product labels, ingredients, 
        and nutritional information.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>Our Vision</h3>
        <p>We believe that everyone deserves access to clear, understandable information about what 
        they're consuming. Our platform uses cutting-edge AI technology to analyze product labels, 
        identify potential health concerns, and provide personalized recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>Key Features</h3>
        <ul>
            <li><strong>AI-Powered Analysis:</strong> Using Google Gemini AI for accurate product analysis</li>
            <li><strong>Nutritional Insights:</strong> Detailed breakdown of nutritional values and health impact</li>
            <li><strong>Ingredient Analysis:</strong> Understand what each ingredient does and its health implications</li>
            <li><strong>Medicine Safety:</strong> Check for drug interactions and safety information</li>
            <li><strong>Barcode Scanning:</strong> Quick product lookup using barcode technology</li>
            <li><strong>Personalized Chatbot:</strong> Get nutrition advice tailored to your needs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>Technology Stack</h3>
        <ul>
            <li>🐍 Python with Streamlit Framework</li>
            <li>🤖 Google Gemini AI for Analysis</li>
            <li>📷 Advanced Image Processing</li>
            <li>📊 Data Visualization with Plotly</li>
            <li>☁️ Cloud-ready Architecture</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='stat-box'>
            <h3>👥</h3>
            <p><strong>User-Centric</strong><br>Built for everyone</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='stat-box'>
            <h3>⚡</h3>
            <p><strong>Fast</strong><br>Instant Analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='stat-box'>
            <h3>🔒</h3>
            <p><strong>Secure</strong><br>Privacy First</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: GUIDELINES
# ============================================================================
def page_guidelines():
    st.markdown("<h1 style='color: #059669;'>📋 Food Guidelines & Regulations</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🏛️ Nutritional Guidelines</h3>
        <p>Understanding food labels and nutritional guidelines helps you make better dietary choices. 
        Here are the key nutritional guidelines recommended by health authorities:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h4>Daily Intake Recommendations</h4>
            <ul>
                <li><strong>Calories:</strong> 2000-2500 (varies by age/activity)</li>
                <li><strong>Protein:</strong> 50-60g (10-15% of calories)</li>
                <li><strong>Carbohydrates:</strong> 225-325g (45-65% of calories)</li>
                <li><strong>Fats:</strong> 44-78g (20-35% of calories)</li>
                <li><strong>Fiber:</strong> 25-35g daily</li>
                <li><strong>Water:</strong> 8-10 glasses daily</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h4>Nutrients to Limit</h4>
            <ul>
                <li><strong>Added Sugar:</strong> Less than 25-36g daily</li>
                <li><strong>Sodium:</strong> Less than 2300mg daily</li>
                <li><strong>Saturated Fat:</strong> Less than 20g daily</li>
                <li><strong>Trans Fat:</strong> Avoid completely</li>
                <li><strong>Cholesterol:</strong> Less than 300mg daily</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🏷️ Food Labeling Standards</h3>
        <p><strong>FDA Nutrition Facts Label Requirements:</strong></p>
        <ul>
            <li>Serving size must be clearly stated</li>
            <li>Calories per serving must be prominently displayed</li>
            <li>List of 13 nutrients (mandatory)</li>
            <li>Ingredient list in descending order by weight</li>
            <li>Allergen information clearly marked</li>
            <li>Expiration date and storage instructions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🥗 Good Food Habits</h3>
        <ul>
            <li>✅ Choose whole grains over refined grains</li>
            <li>✅ Eat plenty of fruits and vegetables (5+ servings daily)</li>
            <li>✅ Choose lean proteins (fish, chicken, beans)</li>
            <li>✅ Limit processed and ultra-processed foods</li>
            <li>✅ Stay hydrated with water</li>
            <li>✅ Control portion sizes</li>
            <li>✅ Read nutrition labels before buying</li>
            <li>✅ Plan meals ahead</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: HELPLINES
# ============================================================================
def page_helplines():
    st.markdown("<h1 style='color: #059669;'>📞 Health & Support Helplines</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🆘 Emergency Services</h3>
        <ul>
            <li><strong>Ambulance/Emergency:</strong> 102 (India)</li>
            <li><strong>Police Emergency:</strong> 100 (India)</li>
            <li><strong>Fire Service:</strong> 101 (India)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🏥 Health Helplines - India</h3>
        <ul>
            <li><strong>National Health Service Helpline:</strong> 1075</li>
            <li><strong>AYUSH Helpline:</strong> 1800-180-1104</li>
            <li><strong>National Poison Control Center:</strong> 011-4060-7600</li>
            <li><strong>NAMS Helpline:</strong> 1800-181-8111</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🧠 Mental Health Support</h3>
        <ul>
            <li><strong>AASRA Suicide Helpline:</strong> 9820466726</li>
            <li><strong>iCall Helpline:</strong> 9152987821</li>
            <li><strong>Vandrevala Foundation:</strong> 9999-666-555</li>
            <li><strong>ECHO Helpline:</strong> 011-4141-4141</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>💊 Pharmacy & Medicine</h3>
        <ul>
            <li><strong>Poison Information Helpline:</strong> 011-4060-7600</li>
            <li><strong>Drug Regulatory Authority:</strong> 1800-123-4444</li>
            <li><strong>Medicines Safety Reporting:</strong> Visit www.ipc.gov.in</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🌍 International Helplines</h3>
        <ul>
            <li><strong>WHO Helpline:</strong> +41 22 791 2111</li>
            <li><strong>International Poison Control:</strong> +1-202-462-2882</li>
            <li><strong>FDA Adverse Event Reporting:</strong> 1-888-SAFEFOOD</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: #fef3c7; padding: 15px; border-radius: 8px; border-left: 4px solid #f59e0b; margin-top: 20px;'>
        <p><strong>⚠️ Disclaimer:</strong> This platform is for informational purposes only. 
        In case of medical emergencies, please contact your nearest hospital or emergency services. 
        Always consult with healthcare professionals for medical advice.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE ROUTING
# ============================================================================
def main():
    # Route to appropriate page based on session state
    if st.session_state.page == "Home":
        page_home()
    elif st.session_state.page == "Label_Analyzer":
        page_label_analyzer()
    elif st.session_state.page == "Barcode_Scanner":
        page_barcode_scanner()
    elif st.session_state.page == "Chatbot":
        page_chatbot()
    elif st.session_state.page == "Medicine_Checker":
        page_medicine_checker()
    elif st.session_state.page == "About":
        page_about()
    elif st.session_state.page == "Guidelines":
        page_guidelines()
    elif st.session_state.page == "Helplines":
        page_helplines()

if __name__ == "__main__":
    main()
