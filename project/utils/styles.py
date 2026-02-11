"""
Custom Styling Module for Label Padega Sabh

This module contains all custom CSS styling for the Streamlit application.
Import and call apply_custom_styles() in main.py to apply the theme.
"""

import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styling to the entire app"""
    st.markdown("""
    <style>
        /* ============================================================
           COLOR SCHEME
           ============================================================ */
        :root {
            --primary-color: #059669;      /* Emerald Green */
            --secondary-color: #027353;    /* Dark Green */
            --accent-color: #38a169;       /* Fresh Green */
            --light-bg: #f0fdf4;          /* Light Green */
            --text-color: #1f2937;        /* Dark Gray */
            --success-color: #4CAF50;     /* Success Green */
            --warning-color: #FFC107;     /* Warning Orange */
            --danger-color: #F44336;      /* Danger Red */
        }

        /* ============================================================
           TYPOGRAPHY & HEADINGS
           ============================================================ */
        .main-header {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #2E7D32;
            font-weight: 700;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }

        .sub-header {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #424242;
            font-weight: 400;
        }

        h1 {
            color: #059669;
            border-bottom: 2px solid #059669;
            padding-bottom: 10px;
        }

        h2 {
            color: #027353;
            margin-top: 20px;
            padding-top: 10px;
        }

        h3, h4 {
            color: #38a169;
        }

        /* ============================================================
           CARDS & CONTAINERS
           ============================================================ */
        .feature-card {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid #059669;
            margin: 10px 0;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(5, 150, 105, 0.1);
        }

        .feature-card:hover {
            box-shadow: 0 4px 12px rgba(5, 150, 105, 0.2);
            transform: translateX(5px);
        }

        .highlight-box {
            background-color: #f0f8ff;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #388E3C;
            margin-bottom: 20px;
        }

        .stat-box {
            background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #a7f3d0;
            transition: all 0.3s ease;
        }

        .stat-box:hover {
            box-shadow: 0 4px 12px rgba(5, 150, 105, 0.15);
        }

        .stat-value {
            font-size: 28px;
            font-weight: 700;
            color: #059669;
        }

        .stat-label {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }

        /* ============================================================
           STATUS BOXES
           ============================================================ */
        .success-box {
            background-color: #E8F5E9;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #43a047;
            margin-bottom: 20px;
        }

        .warning-box {
            background-color: #FFF8E1;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #ffb300;
            margin-bottom: 20px;
        }

        .danger-box {
            background-color: #FFEBEE;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #e53935;
            margin-bottom: 20px;
        }

        .info-box {
            background-color: #E1F5FE;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #1976d2;
            margin-bottom: 20px;
        }

        /* ============================================================
           METRIC DISPLAYS
           ============================================================ */
        .metric-card {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            margin: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .metric-value {
            font-size: 32px;
            font-weight: 700;
            color: #1E88E5;
            margin: 10px 0;
        }

        .metric-label {
            font-size: 14px;
            color: #616161;
            font-weight: 600;
        }

        /* ============================================================
           BUTTONS & INTERACTIONS
           ============================================================ */
        .stButton > button {
            background-color: #059669;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #027353;
            box-shadow: 0 4px 8px rgba(5, 150, 105, 0.3);
        }

        /* ============================================================
           TABS & SECTIONS
           ============================================================ */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #E8F5E9;
            border-radius: 4px 4px 0px 0px;
            padding-top: 10px;
            padding-bottom: 10px;
            color: #424242;
            transition: all 0.3s ease;
        }

        .stTabs [aria-selected="true"] {
            background-color: #059669;
            color: white;
        }

        /* ============================================================
           FORMS & INPUTS
           ============================================================ */
        .stTextInput input {
            border: 2px solid #d1fae5 !important;
            border-radius: 8px !important;
        }

        .stTextInput input:focus {
            border-color: #059669 !important;
            box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.1) !important;
        }

        .stSelectbox select {
            border: 2px solid #d1fae5 !important;
            border-radius: 8px !important;
        }

        .stFileUploadDropzone {
            border: 2px dashed #059669 !important;
            border-radius: 8px !important;
            background-color: #f0fdf4 !important;
        }

        /* ============================================================
           SIDEBAR
           ============================================================ */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f0fdf4 0%, #dcfce7 100%);
        }

        [data-testid="stSidebar"] button {
            width: 100%;
            background-color: #e8f5e9 !important;
            color: #059669 !important;
            border: 2px solid #a7f3d0 !important;
            border-radius: 8px !important;
            margin: 5px 0 !important;
            transition: all 0.3s ease !important;
        }

        [data-testid="stSidebar"] button:hover {
            background-color: #059669 !important;
            color: white !important;
            transform: scale(1.02) !important;
        }

        /* ============================================================
           DIVIDERS & SEPARATORS
           ============================================================ */
        hr {
            border-color: #d1fae5 !important;
            margin: 20px 0 !important;
        }

        /* ============================================================
           EXPANDABLE SECTIONS
           ============================================================ */
        .streamlit-expanderHeader {
            background-color: #e8f5e9;
            border-radius: 8px;
            padding: 10px;
        }

        .streamlit-expanderHeader:hover {
            background-color: #d1fae5;
        }

        /* ============================================================
           TEXT STYLES
           ============================================================ */
        .highlight {
            background-color: #fef3c7;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 600;
            color: #d97706;
        }

        code {
            background-color: #f3f4f6;
            padding: 2px 6px;
            border-radius: 4px;
            color: #d946ef;
        }

        /* ============================================================
           IMAGES & MEDIA
           ============================================================ */
        img {
            border-radius: 8px;
            max-width: 100%;
            height: auto;
            transition: all 0.3s ease;
        }

        img:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        /* ============================================================
           RESPONSIVE DESIGN
           ============================================================ */
        @media (max-width: 768px) {
            .stat-box {
                padding: 10px;
                margin: 5px 0;
            }

            .metric-value {
                font-size: 24px;
            }

            .feature-card {
                padding: 15px;
                margin: 5px 0;
            }
        }

        /* ============================================================
           ANIMATIONS
           ============================================================ */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .fade-in {
            animation: fadeIn 0.3s ease-in-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-10px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .slide-in {
            animation: slideIn 0.3s ease-in-out;
        }

        /* ============================================================
           SCROLLBAR STYLING
           ============================================================ */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }

        ::-webkit-scrollbar-thumb {
            background: #059669;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #027353;
        }
    </style>
    """, unsafe_allow_html=True)


def get_theme_colors():
    """Return a dictionary of theme colors for use in plots, etc."""
    return {
        "primary": "#059669",
        "secondary": "#027353",
        "accent": "#38a169",
        "light_bg": "#f0fdf4",
        "text": "#1f2937",
        "success": "#4CAF50",
        "warning": "#FFC107",
        "danger": "#F44336",
    }
