"""
Label Padega Sabh - Feature Modules Package

This package contains the individual feature modules for the Streamlit application.
Each module can be imported and called from main.py.

Modules:
    - finalanalyzerbot: Food Label Analyzer using AI
    - barcode: Barcode Scanner with product information
    - chatbot: Nutrition Chatbot with AI responses
    - medicines: Medicine Safety Checker

Usage:
    from pages.finalanalyzerbot import run_label_analyzer
    run_label_analyzer()
"""

__version__ = "1.0.0"
__author__ = "Label Padega Sabh Team"

# Import feature functions for easy access
try:
    from pages.finalanalyzerbot import run_label_analyzer
except ImportError:
    pass

try:
    from pages.barcode import run_barcode_scanner
except ImportError:
    pass

try:
    from pages.chatbot import run_nutrition_chatbot
except ImportError:
    pass

try:
    from pages.medicines import run_medicine_analyzer
except ImportError:
    pass

__all__ = [
    "run_label_analyzer",
    "run_barcode_scanner",
    "run_nutrition_chatbot",
    "run_medicine_analyzer"
]
