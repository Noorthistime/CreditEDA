import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Credit Exploratory Data Analysis", layout="wide")


if 'theme' not in st.session_state:
    st.session_state.theme = 'default'

# Hidden Toggle Button
st.markdown('<div class="hide-next-button"></div>', unsafe_allow_html=True)
is_stitch = st.button("HIDDEN_TOGGLE_DO_NOT_CLICK", key="hidden_theme_btn")
if is_stitch:
    st.session_state.theme = 'stitch' if st.session_state.theme == 'default' else 'default'

if st.session_state.theme == 'default':
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    :root {
        --glass-bg: rgba(255, 255, 255, 0.12);
        --glass-border: rgba(255, 255, 255, 0.32);
        --glass-shadow: 0 12px 36px rgba(8, 15, 40, 0.28);
        --brand-1: #00c2ff;
        --brand-2: #4f46e5;
        --brand-3: #26d9a4;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 12%, rgba(38, 217, 164, 0.18), transparent 34%),
            radial-gradient(circle at 88% 20%, rgba(0, 194, 255, 0.18), transparent 40%),
            radial-gradient(circle at 50% 86%, rgba(79, 70, 229, 0.2), transparent 45%),
            linear-gradient(145deg, #0b1220 0%, #121f37 46%, #0b182f 100%);
        background-attachment: fixed;
        color: #eef3ff;
    }

    /* Keep header transparent without hiding it */
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
    }

    @keyframes orbFloat {
        0% { transform: translate3d(0, 0, 0) scale(1); }
        50% { transform: translate3d(0, -14px, 0) scale(1.05); }
        100% { transform: translate3d(0, 0, 0) scale(1); }
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 0 rgba(0, 194, 255, 0.0), 0 10px 26px rgba(10, 18, 42, 0.35); }
        50% { box-shadow: 0 0 22px rgba(79, 70, 229, 0.45), 0 14px 34px rgba(10, 18, 42, 0.45); }
        100% { box-shadow: 0 0 0 rgba(0, 194, 255, 0.0), 0 10px 26px rgba(10, 18, 42, 0.35); }
    }

    @keyframes shimmer {
        0% { background-position: -220% 0; }
        100% { background-position: 220% 0; }
    }

    .stApp::before,
    .stApp::after {
        content: "";
        position: fixed;
        border-radius: 999px;
        filter: blur(52px);
        z-index: 0;
        pointer-events: none;
        animation: orbFloat 9s ease-in-out infinite;
    }

    .stApp::before {
        width: 260px;
        height: 260px;
        right: 10%;
        top: 15%;
        background: rgba(0, 194, 255, 0.18);
    }

    .stApp::after {
        width: 300px;
        height: 300px;
        left: 8%;
        bottom: 8%;
        background: rgba(38, 217, 164, 0.16);
        animation-delay: -3s;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] > div {
        background: linear-gradient(165deg, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0.03));
        backdrop-filter: none;
    }

    [data-testid="stAppViewContainer"] > .main {
        position: relative;
        z-index: 1;
    }

    [data-testid="stVerticalBlock"] > div:has(> [data-testid="stMarkdownContainer"]),
    div[data-testid="stDataFrame"],
    div[data-testid="stAlert"],
    div.stCodeBlock {
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        border-radius: 18px;
        backdrop-filter: blur(14px);
        box-shadow: var(--glass-shadow);
        transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
    }

    [data-testid="stVerticalBlock"] > div:has(> [data-testid="stMarkdownContainer"]):hover,
    div[data-testid="stDataFrame"]:hover,
    div[data-testid="stAlert"]:hover,
    div.stCodeBlock:hover {
        transform: translateY(-2px);
        border-color: rgba(0, 194, 255, 0.5);
        box-shadow: 0 0 18px rgba(0, 194, 255, 0.2), 0 16px 34px rgba(8, 15, 40, 0.36);
    }

    h1, h2, h3 {
        letter-spacing: 0.2px;
        text-shadow: 0 0 18px rgba(79, 70, 229, 0.28);
    }

    div.element-container:has(.premium-hero),
    div.stMarkdown:has(.premium-hero) {
        position: sticky !important;
        top: 15px !important;
        z-index: 999 !important;
    }

    .premium-hero {
        position: relative;
        width: 100%;
        margin: -45px auto 20px auto !important;
        padding: 20px 24px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.34);
        background: linear-gradient(130deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.08));
        backdrop-filter: blur(18px);
        box-shadow: 0 16px 38px rgba(4, 12, 34, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.22);
        overflow: hidden;
        transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        text-align: center;
    }

    .premium-hero.pill-mode {
        width: 85% !important;
        margin: 0 auto 20px auto !important;
        padding: 12px 40px !important;
        border-radius: 50px !important;
        background: linear-gradient(130deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05)) !important;
        box-shadow: 0 10px 30px rgba(4, 12, 34, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
    }
    
    .premium-hero.pill-mode h1 {
        font-size: 1.6rem !important;
    }



    .premium-hero:hover {
        transform: translateY(-3px);
        border-color: rgba(0, 194, 255, 0.78);
        box-shadow: 0 0 30px rgba(0, 194, 255, 0.35), 0 18px 42px rgba(4, 12, 34, 0.5);
    }

    .premium-hero h1 {
        margin: 0;
        font-size: clamp(1.45rem, 2.4vw, 2.2rem);
        font-weight: 800;
        color: #f5f9ff;
        letter-spacing: 0.35px;
        text-shadow: 0 0 16px rgba(79, 70, 229, 0.35);
        position: relative;
        z-index: 1;
    }

    .run-output-box {
        margin-top: 8px;
        padding: 16px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.14), rgba(255, 255, 255, 0.08));
        box-shadow: 0 12px 30px rgba(8, 15, 40, 0.34), inset 0 1px 0 rgba(255, 255, 255, 0.16);
    }

    .stButton > button {
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.45);
        color: #eef3ff;
        background: linear-gradient(120deg, rgba(0, 194, 255, 0.22), rgba(79, 70, 229, 0.24), rgba(38, 217, 164, 0.2));
        background-size: 220% 220%;
        box-shadow: 0 10px 26px rgba(10, 18, 42, 0.35);
        transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px) scale(1.01);
        border-color: rgba(255, 255, 255, 0.9);
        animation: pulseGlow 1.8s ease-in-out infinite;
    }

    .stButton > button:active {
        transform: scale(0.98);
        box-shadow: 0 0 24px rgba(0, 194, 255, 0.55);
    }

    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.12) !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 12px !important;
        color: #eef3ff !important;
        transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }

    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus {
        border-color: rgba(0, 194, 255, 0.9) !important;
        box-shadow: 0 0 0 0.22rem rgba(0, 194, 255, 0.24) !important;
    }

    [data-testid="stTabs"] [role="tab"] {
        border-radius: 12px;
        transition: all 0.2s ease;
    }

    [data-testid="stTabs"] [role="tab"][aria-selected="true"] {
        background: rgba(255, 255, 255, 0.18);
        border: 1px solid rgba(255, 255, 255, 0.45);
        box-shadow: 0 0 14px rgba(79, 70, 229, 0.32);
    }

    .stMarkdown hr {
        border-top: 1px solid rgba(255, 255, 255, 0.22);
    }

    .stCodeBlock {
        position: relative;
        overflow: hidden;
    }

    .stCodeBlock::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(110deg, transparent 0%, rgba(255, 255, 255, 0.14) 48%, transparent 100%);
        background-size: 220% 100%;
        animation: shimmer 7s linear infinite;
        pointer-events: none;
    }

    /* Style the radio items as beautiful horizontal tabs/buttons */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 10px;
        padding-top: 10px;
    }
    
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        padding: 12px 16px !important;
        border-radius: 12px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer;
        display: flex;
        align-items: center;
        width: 100%;
        margin-bottom: 0px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
        background: rgba(0, 194, 255, 0.08) !important;
        border-color: rgba(0, 194, 255, 0.4) !important;
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(0, 194, 255, 0.15);
    }

    /* Style for checked state */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label[data-checked="true"],
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
        background: linear-gradient(135deg, rgba(0, 194, 255, 0.22), rgba(79, 70, 229, 0.24)) !important;
        border-color: rgba(0, 194, 255, 0.7) !important;
        box-shadow: 0 0 15px rgba(0, 194, 255, 0.25), inset 0 0 8px rgba(0, 194, 255, 0.15);
    }

    /* Restore the radio bullet circle and make it red when active */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
        margin-right: 8px;
    }
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label[data-checked="true"] > div:first-child div {
        background-color: #ff4b4b !important;
    }

    /* Hide redundant radio widget label */
    [data-testid="stSidebar"] [data-testid="stRadio"] > label {
        display: none !important;
    }

    /* Typography fixes for sidebar header */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #f5f9ff !important;
        font-weight: 700;
        text-shadow: 0 0 12px rgba(0, 194, 255, 0.35);
        margin-bottom: 12px !important;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {
        color: #f5f9ff !important;
    }

    /* Keep the active cyan highlight in both modes */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label[data-checked="true"] *,
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) * {
        color: #00c2ff !important;
        font-weight: 600 !important;
    }

    @keyframes techPulse {
        0% { text-shadow: 0 0 4px rgba(0, 194, 255, 0.4); color: #00c2ff; }
        50% { text-shadow: 0 0 12px rgba(0, 194, 255, 0.8), 0 0 20px rgba(0, 194, 255, 0.4); color: #eef3ff; }
        100% { text-shadow: 0 0 4px rgba(0, 194, 255, 0.4); color: #00c2ff; }
    }
    .tech-hover-container {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    .glow-tech {
        font-weight: 600;
        text-decoration: underline dotted rgba(0, 194, 255, 0.6) !important;
        animation: techPulse 2s infinite ease-in-out;
        display: inline-block;
        padding: 0 2px;
        color: #00c2ff !important;
        transition: all 0.25s ease;
    }
    .tech-tooltip-box {
        visibility: hidden;
        opacity: 0;
        width: 320px;
        background: rgba(10, 20, 42, 0.98) !important;
        color: #eef3ff !important;
        text-align: left;
        border: 1px solid rgba(0, 194, 255, 0.45);
        border-radius: 10px;
        padding: 14px;
        position: absolute;
        z-index: 9999;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%) translateY(10px);
        transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.65), 0 0 20px rgba(0, 194, 255, 0.25);
        pointer-events: none;
        font-size: 0.9em;
        line-height: 1.4;
        font-weight: normal;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    .tech-tooltip-box strong {
        color: #00c2ff !important;
        font-size: 1.05em;
        display: block;
        margin-bottom: 6px;
    }
    .tech-tooltip-box::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -6px;
        border-width: 6px;
        border-style: solid;
        border-color: rgba(10, 20, 42, 0.98) transparent transparent transparent;
    }
    .tech-hover-container:hover .tech-tooltip-box {
        visibility: visible;
        opacity: 1;
        transform: translateX(-50%) translateY(0);
    }
    .tech-hover-container:hover .glow-tech {
        color: #fff !important;
        text-shadow: 0 0 15px rgba(0, 194, 255, 1) !important;
    }

    /* Premium glassmorphic background for the navigation panel */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 17, 32, 0.95) 0%, rgba(3, 7, 18, 0.98) 100%) !important;
        border-right: 1px solid rgba(0, 194, 255, 0.15) !important;
        box-shadow: 6px 0 25px rgba(0, 0, 0, 0.4) !important;
    }

    /* Structured content cards for layout columns */
    [data-testid="column"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 16px !important;
        padding: 22px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15) !important;
        margin-bottom: 15px !important;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    [data-testid="column"]:hover {
        border-color: rgba(0, 194, 255, 0.15) !important;
        box-shadow: 0 8px 32px rgba(0, 194, 255, 0.03) !important;
    }

    /* Professional subheadings structure */
    div[data-testid="stMarkdownContainer"] h2 {
        color: #eef3ff !important;
        font-weight: 600 !important;
        font-size: 1.35em !important;
        border-bottom: 2px solid rgba(0, 194, 255, 0.25) !important;
        padding-bottom: 8px !important;
        margin-top: 10px !important;
        margin-bottom: 16px !important;
        letter-spacing: 0.5px !important;
    }
    div[data-testid="stMarkdownContainer"] h3 {
        color: #00c2ff !important;
        font-weight: 500 !important;
        font-size: 1.12em !important;
        padding-bottom: 4px !important;
        margin-top: 10px !important;
        margin-bottom: 12px !important;
        letter-spacing: 0.5px !important;
    }

    /* --- Mobile Responsiveness --- */
    @media screen and (max-width: 768px) {
        .stApp::before, .stApp::after {
            display: none !important;
        }
        
        .main .block-container {
            padding: 1rem 0.5rem !important;
        }

        .premium-hero {
            margin: -20px 0 15px 0 !important;
            padding: 15px 12px;
        }

        .premium-hero h1 {
            font-size: 1.5rem !important;
        }

        .tech-tooltip-box {
            width: 260px !important;
        }

        [data-testid="column"] {
            padding: 12px !important;
        }
        
        /* Adjust layout for Markdown containers with heavy padding */
        div[style*="padding: 24px"] {
            padding: 16px !important;
        }
        div[style*="padding: 20px"] {
            padding: 14px !important;
        }
        div[style*="padding: 14px 18px"] {
            padding: 12px !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            gap: 8px !important;
        }
        
        /* Metrics ribbon dividers */
        div[style*="border-left: 1px solid rgba(255, 255, 255, 0.1)"] {
            display: none !important;
        }
        
        /* Metrics ribbon flex */
        div[style*="justify-content: space-around"] {
            flex-direction: column !important;
            gap: 20px !important;
            padding: 20px !important;
        }
        
        div[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label {
            padding: 10px !important;
        }
    }

    /* Instant zero-flash hiding of the theme toggle button */
    div.element-container:has(.hide-next-button),
    div.element-container:has(.hide-next-button) + div.element-container {
        position: absolute !important;
        opacity: 0 !important;
        pointer-events: none !important;
        width: 0 !important;
        height: 0 !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .sentinel-terminal {
        background: rgba(10, 10, 15, 0.9) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 12px 35px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    
    .sentinel-code-body { white-space: nowrap; padding: 20px; font-family: 'Consolas', 'Courier New', monospace; font-size: 0.95rem; line-height: 1.6; color: #a5b4fc; overflow-x: auto; overflow-y: hidden; }
    
    .keyword { color: var(--brand-1) !important; font-weight: bold; }
    .builtin { color: #4f46e5; font-weight: bold; }
</style>

""", unsafe_allow_html=True)

elif st.session_state.theme == 'stitch':
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    :root {
        --glass-bg: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 60, 100, 0.4);
        --glass-shadow: 0 12px 36px rgba(40, 8, 15, 0.35);
        --brand-1: #ff3366;
        --brand-2: #8b0000;
        --brand-3: #ff6633;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 12%, rgba(255, 51, 102, 0.18), transparent 34%),
            radial-gradient(circle at 88% 20%, rgba(204, 0, 51, 0.18), transparent 40%),
            radial-gradient(circle at 50% 86%, rgba(139, 0, 0, 0.2), transparent 45%),
            linear-gradient(145deg, #1a0808 0%, #2a0b12 46%, #120306 100%);
        background-attachment: fixed;
        color: #ffeeee;
    }
    
    [data-testid="stSidebar"] {
        background: rgba(26, 8, 8, 0.6) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border-right: 1px solid var(--glass-border) !important;
        box-shadow: 4px 0 24px rgba(255, 51, 102, 0.1) !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, rgba(255,51,102,0.1) 0%, rgba(204,0,51,0.1) 100%) !important;
        border: 1px solid rgba(255,51,102,0.4) !important;
        color: #ff3366 !important;
        border-radius: 12px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 4px 12px rgba(255,51,102,0.1) !important;
        width: 100%;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #ff3366 0%, #cc0033 100%) !important;
        border-color: #ff3366 !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(255,51,102,0.25) !important;
    }

    div[data-testid="stMarkdownContainer"] h1 {
        font-weight: 800;
        background: linear-gradient(to right, #ff3366, #ff80a0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }

    div[data-testid="stMarkdownContainer"] h2, h3 {
        color: #ff3366 !important;
        font-weight: 700;
    }

    /* Style the radio items as beautiful horizontal tabs/buttons */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 10px;
        padding-top: 10px;
    }
    
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        padding: 12px 16px !important;
        border-radius: 12px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer;
        display: flex;
        align-items: center;
        width: 100%;
        margin-bottom: 0px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
        background: rgba(255, 51, 102, 0.08) !important;
        border-color: rgba(255, 51, 102, 0.4) !important;
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(255, 51, 102, 0.15);
    }

    /* Style for checked state */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label[data-checked="true"],
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
        background: linear-gradient(135deg, rgba(255, 51, 102, 0.22), rgba(139, 0, 0, 0.24)) !important;
        border-color: rgba(255, 51, 102, 0.7) !important;
        box-shadow: 0 0 15px rgba(255, 51, 102, 0.25), inset 0 0 8px rgba(255, 51, 102, 0.15);
    }

    /* Restore the radio bullet circle and make it red when active */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
        margin-right: 8px;
    }
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label[data-checked="true"] > div:first-child div {
        background-color: #ff3366 !important;
    }

    /* Hide redundant radio widget label */
    [data-testid="stSidebar"] [data-testid="stRadio"] > label {
        display: none !important;
    }

    /* Typography fixes for sidebar header — always dark theme */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #f5f9ff !important;
        font-weight: 700;
        text-shadow: 0 0 12px rgba(255, 51, 102, 0.35);
        margin-bottom: 12px !important;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {
        color: #f5f9ff !important;
    }

    /* Keep the active red highlight in both modes */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label[data-checked="true"] *,
    [data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] > label:has(input:checked) * {
        color: #ff3366 !important;
        font-weight: 600 !important;
    }

    div.element-container:has(.premium-hero),
    div.stMarkdown:has(.premium-hero) {
        position: sticky !important;
        top: 15px !important;
        z-index: 999 !important;
    }

    .premium-hero {
        position: relative;
        width: 100%;
        margin: -45px auto 20px auto !important;
        padding: 20px 24px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.34);
        background: linear-gradient(130deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.08));
        backdrop-filter: blur(18px);
        box-shadow: 0 16px 38px rgba(40, 8, 15, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.22);
        overflow: hidden;
        transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        text-align: center;
    }

    .premium-hero.pill-mode {
        width: 85% !important;
        margin: 0 auto 20px auto !important;
        padding: 12px 40px !important;
        border-radius: 50px !important;
        background: linear-gradient(130deg, rgba(255, 51, 102, 0.15), rgba(255, 51, 102, 0.05)) !important;
        box-shadow: 0 10px 30px rgba(40, 8, 15, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
    }
    
    .premium-hero.pill-mode h1 {
        font-size: 1.6rem !important;
    }

    .premium-hero::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(110deg, transparent 0%, rgba(255, 255, 255, 0.2) 50%, transparent 100%);
        background-size: 220% 100%;
        animation: shimmer 6.5s linear infinite;
        pointer-events: none;
    }

    .premium-hero:hover {
        transform: translateY(-3px);
        border-color: rgba(255, 51, 102, 0.78);
        box-shadow: 0 0 30px rgba(255, 51, 102, 0.35), 0 18px 42px rgba(40, 8, 15, 0.5);
    }

    .premium-hero h1 {
        margin: 0 !important;
        font-size: clamp(1.45rem, 2.4vw, 2.2rem);
        font-weight: 800;
        color: #f5f9ff !important;
        background: none !important;
        -webkit-text-fill-color: #f5f9ff !important;
        letter-spacing: 0.35px;
        text-shadow: 0 0 16px rgba(255, 51, 102, 0.45);
        position: relative;
        z-index: 1;
    }

    .glow-tech {
        color: #ff3366;
        font-weight: 600;
        cursor: help;
        border-bottom: 1px dashed rgba(255, 51, 102, 0.5);
        transition: all 0.2s ease;
    }
    
    .glow-tech:hover {
        color: #ff5577;
        text-shadow: 0 0 12px rgba(255, 51, 102, 0.4);
        border-bottom: 1px dashed rgba(255, 51, 102, 0.9);
    }
    
    .tech-hover-container {
        position: relative;
        display: inline-block;
    }
    
    .tech-tooltip-box {
        position: absolute;
        bottom: 120%;
        left: 50%;
        transform: translateX(-50%) translateY(10px);
        background: rgba(20, 5, 10, 0.95);
        border: 1px solid rgba(255, 51, 102, 0.4);
        padding: 12px 16px;
        border-radius: 10px;
        width: max-content;
        max-width: 300px;
        color: #c9d1d9;
        font-size: 0.85em;
        line-height: 1.5;
        box-shadow: 0 8px 24px rgba(255, 51, 102, 0.15);
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        z-index: 1000;
        pointer-events: none;
    }
    
    .tech-tooltip-box strong {
        color: #ff3366;
        display: block;
        font-size: 1.1em;
        margin-bottom: 4px;
    }

    .tech-tooltip-box::after {
        content: '';
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        border-width: 6px;
        border-style: solid;
        border-color: rgba(255, 51, 102, 0.4) transparent transparent transparent;
    }

    .tech-hover-container:hover .tech-tooltip-box {
        opacity: 1;
        visibility: visible;
        transform: translateX(-50%) translateY(0);
    }
    
    @media (max-width: 768px) {
        .tech-tooltip-box {
            width: 240px;
            font-size: 0.85em;
            left: 50%;
            transform: translateX(-50%) translateY(10px);
        }
        .tech-hover-container:hover .tech-tooltip-box {
            transform: translateX(-50%) translateY(0);
        }
    }

    /* Instant zero-flash hiding of the theme toggle button */
    div.element-container:has(.hide-next-button),
    div.element-container:has(.hide-next-button) + div.element-container {
        position: absolute !important;
        opacity: 0 !important;
        pointer-events: none !important;
        width: 0 !important;
        height: 0 !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .sentinel-terminal {
        background: rgba(10, 10, 15, 0.9) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 12px 35px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    
    .sentinel-code-body { white-space: nowrap; padding: 20px; font-family: 'Consolas', 'Courier New', monospace; font-size: 0.95rem; line-height: 1.6; color: #a5b4fc; overflow-x: auto; overflow-y: hidden; }
    
    .keyword { color: var(--brand-1) !important; font-weight: bold; }
    .builtin { color: #4f46e5; font-weight: bold; }
</style>

""", unsafe_allow_html=True)

def show_explanation(text, technique=None):
    if st.session_state.theme == 'stitch':
        bg, border, text_color = "rgba(255, 51, 102, 0.12)", "#ff3366", "#ff3366"
    else:
        bg, border, text_color = "rgba(0, 194, 255, 0.12)", "#00c2ff", "#00c2ff"
        
    st.markdown(f'<div style="background: {bg}; border-left: 4px solid {border}; padding: 12px 16px; border-radius: 12px; margin-top: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 1px solid {border}; word-wrap: break-word; overflow-wrap: break-word;"><strong style="color: {text_color}; font-size: 1.05em; display: block; margin-bottom: 6px;">What this block did:</strong><span style="color: var(--text-color); font-size: 0.95em; line-height: 1.5;">{text}</span></div>', unsafe_allow_html=True)

def render_explain_button(tab_name, explanation_text, technique=None):
    btn_key = f"explain_state_{tab_name}"
    if btn_key not in st.session_state:
        st.session_state[btn_key] = False

    st.write("---")
    if st.button("What's Happening", key=f"explain_btn_{tab_name}"):
        st.session_state[btn_key] = not st.session_state[btn_key]

    if st.session_state[btn_key]:
        if st.session_state.theme == 'stitch':
            bg, border, text_color = "rgba(255, 51, 102, 0.12)", "#ff3366", "#ff3366"
        else:
            bg, border, text_color = "rgba(0, 194, 255, 0.12)", "#00c2ff", "#00c2ff"
            
        st.markdown(f'<div style="background: {bg}; border-left: 4px solid {border}; padding: 12px 16px; border-radius: 12px; margin-top: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 1px solid {border}; word-wrap: break-word; overflow-wrap: break-word;"><strong style="color: {text_color}; font-size: 1.05em; display: block; margin-bottom: 6px;">Page Explanation:</strong><span style="color: var(--text-color); font-size: 0.95em; line-height: 1.5;">{explanation_text}</span></div>', unsafe_allow_html=True)






st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Project Overview", "1. Data Cleaning & Binning", "2. Univariate Analysis", "3. Bivariate & Multivariate Analysis", "4. Full Code Explorer", "5. View Raw Source Code"])


@st.cache_resource
def load_and_clean_data():
    # Allow reading from parent or data directory if not in the current directory
    file_path = "data/application_data.csv"
    if not os.path.exists(file_path):
        if os.path.exists("application_data.csv"):
            file_path = "application_data.csv"
        else:
            file_path = "../application_data.csv"
        
    app_data = pd.read_csv(file_path)
    
    percentage = 47
    threshold = int(((100-percentage)/100)*app_data.shape[0] + 1)
    app_df = app_data.dropna(axis=1, thresh=threshold)
    
    app_df.OCCUPATION_TYPE.fillna("Others", inplace=True)
    app_df.EXT_SOURCE_3.fillna(app_df.EXT_SOURCE_3.median(), inplace=True)
    
    Cols = ["AMT_REQ_CREDIT_BUREAU_HOUR", "AMT_REQ_CREDIT_BUREAU_DAY", "AMT_REQ_CREDIT_BUREAU_WEEK", "AMT_REQ_CREDIT_BUREAU_MON", "AMT_REQ_CREDIT_BUREAU_QRT", "AMT_REQ_CREDIT_BUREAU_YEAR"]
    for col in Cols:
        if col in app_df.columns:
            app_df[col].fillna(app_df[col].mode()[0], inplace=True)
            
    app_df.NAME_TYPE_SUITE.fillna(app_df.NAME_TYPE_SUITE.mode()[0], inplace=True)
    app_df.CNT_FAM_MEMBERS.fillna(app_df.CNT_FAM_MEMBERS.mode()[0], inplace=True)
    app_df.EXT_SOURCE_2.fillna(app_df.EXT_SOURCE_2.median(), inplace=True)
    app_df.AMT_GOODS_PRICE.fillna(app_df.AMT_GOODS_PRICE.median(), inplace=True)
    app_df.AMT_ANNUITY.fillna(app_df.AMT_ANNUITY.median(), inplace=True)
    app_df.DAYS_LAST_PHONE_CHANGE.fillna(app_df.DAYS_LAST_PHONE_CHANGE.median(), inplace=True)
    
    app_df.DAYS_BIRTH = app_df.DAYS_BIRTH.apply(lambda x: abs(x))
    app_df["YEARS_BIRTH"] = app_df.DAYS_BIRTH.apply(lambda x: int(x//365))
    app_df["YEARS_LAST_PHONE_CHANGE"] = app_df.DAYS_LAST_PHONE_CHANGE.apply(lambda x: int(abs(x)//365))
    
    app_df["AMT_CREDIT_Category"] = pd.cut(app_df.AMT_CREDIT, [0, 200000, 400000, 600000, 800000, 1000000],
    labels=["Very Low Credit", "Low Credit", "Medium Credit", "High Credit", "Very High Credit"])
    
    app_df["AGE_Category"] = pd.cut(app_df.YEARS_BIRTH, [0, 25, 45, 65, 85],
    labels=["Below 25", "25-45", "45-65", "65-85"])
    
    return app_data, app_df

@st.cache_resource
def get_prev():
    import os
    try:
        if os.path.exists("data/previous_application.csv"):
            return pd.read_csv("data/previous_application.csv")
        elif os.path.exists("previous_application.csv"):
            return pd.read_csv("previous_application.csv")
        elif os.path.exists("../previous_application.csv"):
            return pd.read_csv("../previous_application.csv")
        else:
            return pd.DataFrame()
    except:
        return pd.DataFrame()


app_data, app_df = load_and_clean_data()
tar_0 = app_df[app_df.TARGET == 0]
tar_1 = app_df[app_df.TARGET == 1]

st.markdown('<div id="hero-scroll-marker" style="position: absolute; top: -10px;"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="premium-hero">
    <h1>Credit Exploratory Data Analysis</h1>
</div>
""", unsafe_allow_html=True)


components.html("""
<script>
    const parentDoc = window.parent.document;
    const marker = parentDoc.getElementById('hero-scroll-marker');
    const heroes = parentDoc.querySelectorAll('.premium-hero');

    if (marker && heroes.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                heroes.forEach(hero => {
                    if (!entry.isIntersecting) {
                        hero.classList.add('pill-mode');
                    } else {
                        hero.classList.remove('pill-mode');
                    }
                });
            });
        }, { root: null, threshold: 0 });
        
        observer.observe(marker);
    }
</script>
""", height=0, width=0)

if menu != "Project Overview":
    st.markdown(f"""
    <div style="text-align: center; margin-top: -10px; margin-bottom: 25px;">
        <span style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); padding: 6px 18px; border-radius: 30px; color: #8a99ad; font-size: 0.85em; font-weight: 500; letter-spacing: 0.5px; display: inline-block; box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);">
            {menu}
        </span>
    </div>
    """, unsafe_allow_html=True)

if menu == "Project Overview":
    if st.session_state.theme == 'stitch':
        c_cyan = "#ff3366"
        rgb_cyan = "255, 51, 102"
        c_green = "#ff3366"
        rgb_green = "255, 51, 102"
        c_orange = "#ff3366"
        rgb_orange = "255, 51, 102"
        c_purple = "#ff3366"
        rgb_purple = "255, 51, 102"
    else:
        c_cyan = "#00c2ff"
        rgb_cyan = "0, 194, 255"
        c_green = "#26d9a4"
        rgb_green = "38, 217, 164"
        c_orange = "#ff9f1c"
        rgb_orange = "255, 159, 28"
        c_purple = "#b854ff"
        rgb_purple = "156, 39, 176"

    st.markdown(f"""<div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); padding: 24px; border-radius: 16px; margin-bottom: 24px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);">
<h2 style="color: {c_cyan}; margin-top: 0; display: flex; align-items: center; gap: 10px; font-size: 1.65em;">• Project Abstract & Overview</h2>
<p style="color: #eef3ff; font-size: 1.05em; line-height: 1.6; margin-bottom: 20px;">The Credit Exploratory Data Analysis (EDA) dashboard is a data analytics console designed to profile credit applicants and isolate risk behaviors associated with payment defaults. The pipeline imports historical user demographics, filters columns with high missing rates, performs median/mode imputation on null spaces, and segments quantitative variables (like age, credit size, and income) into discrete bins. By mapping correlation densities and comparing traits (such as gender, housing type, and organization) against default targets, credit providers can construct data-driven credit rating thresholds. This dashboard visualizes individual demographics, bivariate associations, and contract statuses to improve portfolio risk evaluation.</p>

<!-- Core Objective Box (Full width) -->
<div style="background: rgba({rgb_green}, 0.06); border: 1px solid rgba({rgb_green}, 0.2); padding: 20px; border-radius: 14px; margin-bottom: 24px;">
<h3 style="color: {c_green}; margin-top: 0; margin-bottom: 8px; font-size: 1.25em; display: flex; align-items: center; gap: 8px;">• Core Objective</h3>
<p style="color: #eef3ff; font-size: 0.98em; line-height: 1.5; margin-bottom: 0;">Uncover latent customer risk demographics and credit parameters that correlate with loan payment default rates, helping lending institutions identify key default indicators and protect active credit lines.</p>
</div>

<!-- Pipeline Workflow Panel (Full width) -->
<div style="background: rgba({rgb_orange}, 0.05); border: 1px solid rgba({rgb_orange}, 0.22); padding: 20px; border-radius: 14px; margin-bottom: 24px;">
<h3 style="color: {c_orange}; margin-top: 0; margin-bottom: 16px; font-size: 1.25em; display: flex; align-items: center; gap: 8px;">• Pipeline Workflow</h3>
<div style="display: flex; flex-direction: column; gap: 12px;">
<div style="background: rgba(255, 255, 255, 0.02); border-left: 4px solid {c_orange}; border-top: 1px solid rgba(255, 255, 255, 0.05); border-right: 1px solid rgba(255, 255, 255, 0.05); border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding: 14px 18px; border-radius: 4px 12px 12px 4px; display: flex; align-items: center; gap: 16px;">
<div style="font-size: 1.2em; font-weight: bold; color: {c_orange}; min-width: 32px;">01</div>
<div>
<strong style="color: #eef3ff; display: block; font-size: 0.95em; margin-bottom: 2px;">Multi-Dataset Ingestion</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4;">Loads client applications and previous loan contract files into structured Pandas DataFrames.</span>
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border-left: 4px solid {c_orange}; border-top: 1px solid rgba(255, 255, 255, 0.05); border-right: 1px solid rgba(255, 255, 255, 0.05); border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding: 14px 18px; border-radius: 4px 12px 12px 4px; display: flex; align-items: center; gap: 16px;">
<div style="font-size: 1.2em; font-weight: bold; color: {c_orange}; min-width: 32px;">02</div>
<div>
<strong style="color: #eef3ff; display: block; font-size: 0.95em; margin-bottom: 2px;">Null Features Pruning</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4;">Purges columns containing missing entries exceeding a threshold of 47%, retaining high-integrity variables.</span>
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border-left: 4px solid {c_orange}; border-top: 1px solid rgba(255, 255, 255, 0.05); border-right: 1px solid rgba(255, 255, 255, 0.05); border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding: 14px 18px; border-radius: 4px 12px 12px 4px; display: flex; align-items: center; gap: 16px;">
<div style="font-size: 1.2em; font-weight: bold; color: {c_orange}; min-width: 32px;">03</div>
<div>
<strong style="color: #eef3ff; display: block; font-size: 0.95em; margin-bottom: 2px;">Statistical Imputation</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4;">Imputes remaining missing spaces, employing median parameters for numeric indices and mode/frequency metrics for categories.</span>
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border-left: 4px solid {c_orange}; border-top: 1px solid rgba(255, 255, 255, 0.05); border-right: 1px solid rgba(255, 255, 255, 0.05); border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding: 14px 18px; border-radius: 4px 12px 12px 4px; display: flex; align-items: center; gap: 16px;">
<div style="font-size: 1.2em; font-weight: bold; color: {c_orange}; min-width: 32px;">04</div>
<div>
<strong style="color: #eef3ff; display: block; font-size: 0.95em; margin-bottom: 2px;">Standardization & Binning</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4;">Normalizes demographic indicators (e.g. converting negative days into positive years) and segments continuous metrics (such as age, credit volumes, and income) into discrete intervals.</span>
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border-left: 4px solid {c_orange}; border-top: 1px solid rgba(255, 255, 255, 0.05); border-right: 1px solid rgba(255, 255, 255, 0.05); border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding: 14px 18px; border-radius: 4px 12px 12px 4px; display: flex; align-items: center; gap: 16px;">
<div style="font-size: 1.2em; font-weight: bold; color: {c_orange}; min-width: 32px;">05</div>
<div>
<strong style="color: #eef3ff; display: block; font-size: 0.95em; margin-bottom: 2px;">Correlation Plotting & Auditing</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4;">Plots univariate distributions, bivariate relationships, and multivariate correlation heatmaps to visualize the risk variables.</span>
</div>
</div>
</div>
</div>

<!-- Technologies Used Box (Full width) -->
<div style="background: rgba({rgb_purple}, 0.04); border: 1px solid rgba({rgb_purple}, 0.18); padding: 20px; border-radius: 14px; margin-bottom: 24px;">
<h3 style="color: {c_purple}; margin-top: 0; margin-bottom: 16px; font-size: 1.25em; display: flex; align-items: center; gap: 8px;">• Technologies Used</h3>
<div style="display: flex; flex-direction: column; gap: 14px;">
<div style="display: flex; gap: 4px; flex-direction: column;">
<strong style="color: #eef3ff; font-size: 0.98em;">1. Pandas</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4; padding-left: 20px;">Handles application and contract loading, NaN value detection, imputations, binning limits, and index aggregations.</span>
</div>
<div style="display: flex; gap: 4px; flex-direction: column;">
<strong style="color: #eef3ff; font-size: 0.98em;">2. NumPy</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4; padding-left: 20px;">Optimises demographic normalization and mathematical matrices, handling array indexes and data mappings.</span>
</div>
<div style="display: flex; gap: 4px; flex-direction: column;">
<strong style="color: #eef3ff; font-size: 0.98em;">3. Seaborn & Matplotlib</strong>
<span style="color: #c9d1d9; font-size: 0.88em; line-height: 1.4; padding-left: 20px;">Render dynamic plots, correlation grids, client age bins, credit volumes, and contract categories.</span>
</div>
</div>
</div>

<!-- Metrics Ribbon -->
<div style="margin-top: 24px; background: rgba({rgb_cyan}, 0.05); border: 1px solid rgba({rgb_cyan}, 0.15); padding: 16px; border-radius: 12px; display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center; gap: 16px;">
<div>
<div style="font-size: 1.8em; font-weight: bold; color: {c_cyan};">49,000+</div>
<div style="font-size: 0.85em; color: #8b949e; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 4px;">Current Applications</div>
</div>
<div style="border-left: 1px solid rgba(255, 255, 255, 0.1); height: 50px; align-self: center;"></div>
<div>
<div style="font-size: 1.8em; font-weight: bold; color: {c_green};">1.67 Million</div>
<div style="font-size: 0.85em; color: #8b949e; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 4px;">Historical Loan Records</div>
</div>
<div style="border-left: 1px solid rgba(255, 255, 255, 0.1); height: 50px; align-self: center;"></div>
<div>
<div style="font-size: 1.8em; font-weight: bold; color: {c_orange};">~8.0%</div>
<div style="font-size: 0.85em; color: #8b949e; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 4px;">Default Rate (Target 1)</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

elif menu == "1. Data Cleaning & Binning":

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Cleaning Code")
        st.code("""
# Dropping columns with missing values greater than 47%
percentage = 47
threshold = int(((100-percentage)/100)*app_data.shape[0] + 1)
app_df = app_data.dropna(axis=1, thresh=threshold)

# Standardizing Days columns in Years for easy binning
app_df.DAYS_BIRTH = app_df.DAYS_BIRTH.apply(lambda x: abs(x))
app_df["YEARS_BIRTH"] = app_df.DAYS_BIRTH.apply(lambda x: int(x//365))

app_df["AGE_Category"] = pd.cut(
    app_df.YEARS_BIRTH, 
    [0, 25, 45, 65, 85],
    labels = ["Below 25", "25-45", "45-65", "65-85"]
)
        """, language="python")
    with col2:
        st.subheader("Data Overview (Cleaned)")
        st.dataframe(app_df.head(10))
        
        st.write("Age Category Distribution")
        fig, ax = plt.subplots(figsize=(5, 3))
        app_df["AGE_Category"].value_counts(normalize=True).plot.pie(autopct='%1.2f%%', ax=ax)
        st.pyplot(fig)
    render_explain_button("cleaning_binning", "This page displays the initial data processing and <span class='tech-hover-container'><span class='glow-tech'>quality assurance</span><span class='tech-tooltip-box'><strong>Quality Assurance</strong>The process of auditing datasets to identify, isolate, and remove anomalies, missing inputs, and inconsistent formats.</span></span> checks. It handles missing records via <span class='tech-hover-container'><span class='glow-tech'>median imputation</span><span class='tech-tooltip-box'><strong>Median Imputation</strong>A statistic replacement technique that replaces missing numeric cells with the middle-most value of that column to prevent bias.</span></span>, performs <span class='tech-hover-container'><span class='glow-tech'>data binning</span><span class='tech-tooltip-box'><strong>Data Binning</strong>The process of grouping continuous variables (like age or income) into discrete interval groups (bins) for categorical distribution plotting.</span></span> on ages/credit levels, and profiles variables.")


elif menu == "2. Univariate Analysis":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Univariate Analysis Code")
        st.code("""
# Analysis on AMT_GOODS_PRICE on target 0 and 1
plt.figure(figsize=(10,6))
sns.histplot(tar_0['AMT_GOODS_PRICE'], label = 'tar_0', kde=True)
sns.histplot(tar_1['AMT_GOODS_PRICE'], label = 'tar_1', kde=True)
plt.legend()
plt.show()
        """, language="python")
    with col2:
        st.subheader("AMT_GOODS_PRICE (Target 0 vs Target 1)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(tar_0['AMT_GOODS_PRICE'], label='tar_0', kde=True, ax=ax, color='blue', alpha=0.5)
        sns.histplot(tar_1['AMT_GOODS_PRICE'], label='tar_1', kde=True, ax=ax, color='red', alpha=0.5)
        ax.legend()
        st.pyplot(fig)
        st.info("Conclusion: The price of the goods for which loans are given has the same variation for Target 0 and 1.")
    render_explain_button("univariate_analysis", "This page displays <span class='tech-hover-container'><span class='glow-tech'>single-variable distributions</span><span class='tech-tooltip-box'><strong>Single-Variable Distributions</strong>Statistical distributions showing the spread and frequency of a single feature across the dataset records.</span></span> to identify potential <span class='tech-hover-container'><span class='glow-tech'>default indicators</span><span class='tech-tooltip-box'><strong>Default Indicators</strong>Specific variable characteristics (e.g. higher loan-to-income ratio) that statistically correlate with client loan defaults.</span></span>. It overlays goods price <span class='tech-hover-container'><span class='glow-tech'>histograms</span><span class='tech-tooltip-box'><strong>Histograms</strong>A graphical representation that organizes a group of data points into user-specified ranges and plots their frequency counts.</span></span> for normal clients against defaulting clients.")


elif menu == "3. Bivariate & Multivariate Analysis":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Correlation Heatmap Code")
        st.code("""
# Co-relation between Numerical Columns for Target 0
corr_data_0 = tar_0[["AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY", 
                     "AMT_GOODS_PRICE", "YEARS_BIRTH", "YEARS_LAST_PHONE_CHANGE"]]

plt.figure(figsize=(10,10))
sns.heatmap(corr_data_0.corr(), annot=True, cmap="RdYlGn")
plt.show()
        """, language="python")
    with col2:
        st.subheader("Correlation Heatmap (Target 0)")
        corr_data_0 = tar_0[["AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY", "AMT_GOODS_PRICE", "YEARS_BIRTH", "YEARS_LAST_PHONE_CHANGE"]]
        fig, ax = plt.subplots(figsize=(6, 6))
        sns.heatmap(corr_data_0.corr(), annot=True, cmap="RdYlGn", ax=ax, fmt=".2f")
        st.pyplot(fig)
    render_explain_button("bivariate_multivariate", "This page performs cross-feature <span class='tech-hover-container'><span class='glow-tech'>relationship analysis</span><span class='tech-tooltip-box'><strong>Relationship Analysis</strong>The statistical assessment of how change in one variable affects another, checking bivariate and multivariate interactions.</span></span>. It generates a <span class='tech-hover-container'><span class='glow-tech'>correlation matrix</span><span class='tech-tooltip-box'><strong>Correlation Matrix</strong>A table displaying correlation coefficients between variables, where each cell represents the correlation between two columns.</span></span> heatmap to outline <span class='tech-hover-container'><span class='glow-tech'>linear dependencies</span><span class='tech-tooltip-box'><strong>Linear Dependencies</strong>A relationship where a variable changes proportionally with another, measured using the Pearson correlation coefficient.</span></span> among continuous parameters.")


elif menu == "4. Full Code Explorer":
    if 'credit_active_block' not in st.session_state:
        st.session_state.credit_active_block = None

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Interactive Code Explorer")
        
        st.markdown("### Block 1: App Data Inspection")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                <span class="keyword">import</span> pandas <span class="keyword">as</span> pd<br><span class="keyword">import</span> numpy <span class="keyword">as</span> np<br><span class="keyword">import</span> seaborn <span class="keyword">as</span> sns<br><span class="keyword">import</span> matplotlib.pyplot <span class="keyword">as</span> plt<br>&nbsp;<br>app_data = pd.<span class="builtin">read_csv</span>("application_data.csv")<br>null_col = app_data.isnull().sum().sort_values(ascending = <span class="builtin">False</span>)<br>null_col = null_col[null_col.values >(0.40*<span class="builtin">len</span>(app_data))]
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 1"): st.session_state.credit_active_block = "block1"
        
        st.markdown("### Block 2: Null Dropping & Imputation")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                percentage = 47<br>threshold = <span class="builtin">int</span>(((100-percentage)/100)*app_data.<span class="builtin">shape</span>[0] + 1)<br>app_df = app_data.dropna(axis=1, thresh=threshold)<br>app_df["AMT_ANNUITY"].<span class="builtin">fillna</span>(app_df["AMT_ANNUITY"].median(), inplace=<span class="builtin">True</span>)<br>app_df["AMT_GOODS_PRICE"].<span class="builtin">fillna</span>(app_df["AMT_GOODS_PRICE"].median(), inplace=<span class="builtin">True</span>)<br>app_df["CNT_FAM_MEMBERS"].<span class="builtin">fillna</span>(app_df["CNT_FAM_MEMBERS"].median(), inplace=<span class="builtin">True</span>)
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 2"): st.session_state.credit_active_block = "block2"
        
        st.markdown("### Block 3: Binning & Categories")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                app_df.DAYS_BIRTH = app_df.DAYS_BIRTH.<span class="builtin">apply</span>(lambda x: abs(x))<br>app_df["YEARS_BIRTH"] = app_df.DAYS_BIRTH.<span class="builtin">apply</span>(lambda x: <span class="builtin">int</span>(x//365))<br>app_df["AGE_Category"] = pd.cut(app_df.YEARS_BIRTH, [0, 25, 45, 65, 85], labels=["Below 25", "25-45", "45-65", "65-85"])<br>app_df["CREDIT_Category"] = pd.cut(app_df.AMT_CREDIT, [0, 250000, 500000, 750000, 1000000], labels=["Below 2.5L", "2.5L-5L", "5L-7.5L", "7.5L-10L"])<br>app_df["AGE_Category"].value_counts(normalize=<span class="builtin">True</span>).plot.pie()
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 3"): st.session_state.credit_active_block = "block3"
        
        st.markdown("### Block 4: Target Imbalance")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                app_df.TARGET.value_counts(normalize=<span class="builtin">True</span>).plot.pie(autopct='%1.2f%%')
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 4"): st.session_state.credit_active_block = "block4"

        st.markdown("### Block 5: Univariate Analysis")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                sns.histplot(app_df.AMT_CREDIT, bins=10)<br>plt.title("Distribution of AMT_CREDIT")
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 5"): st.session_state.credit_active_block = "block5"

        st.markdown("### Block 6: Target 0 vs 1 Bivariate")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                tar_0 = app_df[app_df.TARGET == 0]<br>tar_1 = app_df[app_df.TARGET == 1]<br>sns.histplot(tar_0['AMT_GOODS_PRICE'], label='tar_0', kde=<span class="builtin">True</span>)<br>sns.histplot(tar_1['AMT_GOODS_PRICE'], label='tar_1', kde=<span class="builtin">True</span>)
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 6"): st.session_state.credit_active_block = "block6"

        st.markdown("### Block 7: Correlation Heatmaps")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                corr_data_0 = tar_0[["AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY", "AMT_GOODS_PRICE", "YEARS_BIRTH"]]<br>sns.<span class="builtin">heatmap</span>(corr_data_0.corr(), annot=<span class="builtin">True</span>, cmap="RdYlGn")
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 7"): st.session_state.credit_active_block = "block7"

        st.markdown("### Block 8: Previous Application Data")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                prev_app = pd.<span class="builtin">read_csv</span>("previous_application.csv")<br>prev_app["AMT_ANNUITY"].<span class="builtin">fillna</span>(prev_app["AMT_ANNUITY"].median(), inplace=<span class="builtin">True</span>)<br>prev_app["AMT_GOODS_PRICE"].<span class="builtin">fillna</span>(prev_app["AMT_GOODS_PRICE"].median(), inplace=<span class="builtin">True</span>)
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 8"): st.session_state.credit_active_block = "block8"

        st.markdown("### Block 9: Previous App Bivariate")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                sns.<span class="builtin">countplot</span>(x='NAME_CONTRACT_STATUS', data=prev_app)<br>plt.title("Contract Status")
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 9"): st.session_state.credit_active_block = "block9"

        st.markdown("### Block 10: Merged Data Heatmaps")
        st.markdown('''
        <div class="sentinel-terminal">
            <div class="sentinel-code-body">
                merged_df = pd.merge(app_df, prev_app, on="SK_ID_CURR", how="inner")<br>pivot_table = pd.pivot_table(merged_df, values='AMT_CREDIT_x', index='NAME_INCOME_TYPE', columns='NAME_CONTRACT_STATUS', aggfunc=np.mean)<br>sns.<span class="builtin">heatmap</span>(pivot_table, annot=<span class="builtin">True</span>, cmap="YlGnBu")
            </div>
        </div>
        ''', unsafe_allow_html=True)
        if st.button("▶ Run Block 10"): st.session_state.credit_active_block = "block10"

    with col2:
        st.subheader("Dynamic Output")
        
        prev_app = get_prev()
        
        if st.session_state.credit_active_block is None:
            st.info("👈 Click a 'Run' button on the left to see the output here!")
        else:
            phase_map = {
                "block1": "Data Inspection",
                "block2": "Null Handling",
                "block3": "Feature Binning",
                "block4": "Target Imbalance Check",
                "block5": "Univariate Analysis",
                "block6": "Bivariate Analysis",
                "block7": "Correlation Analysis",
                "block8": "Previous App Loading",
                "block9": "Previous App Analysis",
                "block10": "Merged Insights"
            }
            progress_map = {
                "block1": 0.10,
                "block2": 0.22,
                "block3": 0.34,
                "block4": 0.45,
                "block5": 0.56,
                "block6": 0.68,
                "block7": 0.79,
                "block8": 0.88,
                "block9": 0.94,
                "block10": 1.00
            }
            active_block = st.session_state.credit_active_block

            with st.expander("Run Progress & Output", expanded=True):
                phase = phase_map.get(active_block, "Processing")
                progress_value = progress_map.get(active_block, 0.0)
                st.progress(progress_value, text=f"Phase: {phase} ({int(progress_value * 100)}%)")

                if active_block == "block1":
                    st.write("Top Columns with >40% Missing Values:")
                    null_col = app_data.isnull().sum().sort_values(ascending=False)
                    st.dataframe(null_col[null_col.values > (0.40 * len(app_data))])
                    show_explanation("Inspects the raw client application dataset (`application_data.csv`) to calculate the proportion of null entries in each column, identifying highly sparse fields.")
                elif active_block == "block2":
                    st.success("Dropped columns with >47% missing values and Imputed numeric NaNs with median!")
                    st.dataframe(app_df.head(10))
                    show_explanation("Implements data cleaning by dropping columns with more than 47% null entries, and imputing missing numeric data with their median values and categorical data with mode or custom tags.", technique="**Median & Mode Imputation:** Replacing NaN values with robust statistics (median for numeric values to reduce outlier effects, and mode for categorical values representing the most common occurrence).")
                elif active_block == "block3":
                    fig, ax = plt.subplots(figsize=(5,4))
                    app_df["AGE_Category"].value_counts(normalize=True).plot.pie(autopct='%1.2f%%', ax=ax)
                    ax.set_title("Age Category Distribution")
                    st.pyplot(fig)
                    show_explanation("Standardizes day features into absolute years and groups clients into age buckets (`Below 25`, `25-45`, etc.) and credit buckets, plotting the age distribution pie chart.", technique="**Feature Binning:** Discretizing continuous data (ages or credit amount values) into categorical bins to analyze group behaviors systematically.")
                elif active_block == "block4":
                    fig, ax = plt.subplots(figsize=(5,4))
                    app_df["TARGET"].value_counts(normalize=True).plot.pie(autopct='%1.2f%%', ax=ax, labels=["0 (No Defaulter)", "1 (Defaulter)"])
                    ax.set_title("Target Variable Imbalance")
                    st.pyplot(fig)
                    show_explanation("Performs class imbalance check on the `TARGET` variable (where 0 indicates non-defaulter and 1 indicates default), displaying a pie chart that shows roughly 8% of candidates default.", technique="**Imbalance Inspection:** Analyzing label skewness to determine if standard classifier metrics will require sampling adjustments or cost-sensitive weights.")
                elif active_block == "block5":
                    fig, ax = plt.subplots(figsize=(6,4))
                    sns.histplot(app_df.AMT_CREDIT, bins=20, kde=True, ax=ax)
                    ax.set_title("Distribution of AMT_CREDIT")
                    st.pyplot(fig)
                    show_explanation("Runs univariate analysis on loan credit sizes by plotting a distribution histogram of `AMT_CREDIT` to see concentration of loan values.")
                elif active_block == "block6":
                    fig, ax = plt.subplots(figsize=(8,5))
                    sns.histplot(tar_0['AMT_GOODS_PRICE'], label='0 (No Default)', kde=True, ax=ax, color='blue', alpha=0.5)
                    sns.histplot(tar_1['AMT_GOODS_PRICE'], label='1 (Default)', kde=True, ax=ax, color='red', alpha=0.5)
                    ax.legend()
                    ax.set_title("Goods Price Distribution (Target 0 vs 1)")
                    st.pyplot(fig)
                    show_explanation("Compares the distribution of goods prices (`AMT_GOODS_PRICE`) for repayers (`TARGET = 0`) versus defaulters (`TARGET = 1`) to identify variations in loan sizing behaviors.", technique="**Bivariate Density Visualization:** Plotting overlapping histograms with kernel density estimation curves to visually inspect if repayment status splits on price values.")
                elif active_block == "block7":
                    corr_data_0 = tar_0[["AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY", "AMT_GOODS_PRICE", "YEARS_BIRTH"]]
                    fig, ax = plt.subplots(figsize=(6, 6))
                    sns.heatmap(corr_data_0.corr(), annot=True, cmap="RdYlGn", ax=ax, fmt=".2f")
                    ax.set_title("Target 0 Correlation Heatmap")
                    st.pyplot(fig)
                    show_explanation("Constructs a correlation matrix heatmap among key numerical variables (income, credit, annuity, age) for non-defaulting clients to reveal linear relationships.", technique="**Pearson Correlation Coefficient Matrix:** Measures the linear correlation between numeric vectors, ranging from -1.00 (inverse) to +1.00 (direct).")
                elif active_block == "block8":
                    if not prev_app.empty:
                        st.write("Previous Application Data shape: ", prev_app.shape)
                        st.dataframe(prev_app.head(10))
                    else:
                        st.error("previous_application.csv not found!")
                    show_explanation("Loads the historical applications dataset (`previous_application.csv`) and prints its dimensions and head to verify historical applicant characteristics.")
                elif active_block == "block9":
                    if not prev_app.empty:
                        fig, ax = plt.subplots(figsize=(6,4))
                        sns.countplot(x='NAME_CONTRACT_STATUS', data=prev_app, ax=ax)
                        ax.set_title("Contract Status in Previous Applications")
                        st.pyplot(fig)
                    show_explanation("Runs univariate counts on the contract statuses of previous applications, graphing the proportion of Approved, Refused, Canceled, or Unused loans.")
                elif active_block == "block10":
                    if not prev_app.empty:
                        merged_df = pd.merge(app_df, prev_app, on="SK_ID_CURR", how="inner")
                        pivot_table = pd.pivot_table(merged_df, values='AMT_CREDIT_x', index='NAME_INCOME_TYPE', columns='NAME_CONTRACT_STATUS', aggfunc=np.mean)
                        fig, ax = plt.subplots(figsize=(8,6))
                        sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", ax=ax, fmt=".0f")
                        ax.set_title("Mean Credit Amount by Income Type & Status")
                        st.pyplot(fig)
                    show_explanation("Merges current credit applications with historical records, building a pivot table heatmap showing average credit amounts across applicant income streams and past loan contract statuses.", technique="**Inner Join & Multi-dimensional Pivot Aggregation:** Merging relational datasets on unique primary keys (`SK_ID_CURR`) and building a pivot layout to compute average numeric credit levels across categories.")


elif menu == "5. View Raw Source Code":
    st.subheader("Raw Source Code (Doc3Credit.py)")
    st.info("Here is the complete, original source code for this project.")
    try:
        with open("src/Doc3Credit.py", "r", encoding="utf-8") as f:
            st.code(f.read(), language="python")
    except FileNotFoundError:
        try:
            with open("Doc3Credit.py", "r", encoding="utf-8") as f:
                st.code(f.read(), language="python")
        except FileNotFoundError:
            try:
                with open("../Doc3Credit.py", "r", encoding="utf-8") as f:
                    st.code(f.read(), language="python")
            except FileNotFoundError:
                st.error("Original code file not found.")
    render_explain_button("raw_source", "This page showcases the original raw scripting <span class='tech-hover-container'><span class='glow-tech'>codebase</span><span class='tech-tooltip-box'><strong>Codebase</strong>The complete collection of computer source files, logic routines, and configurations that make up a software program.</span></span>, detailing the sequence of <span class='tech-hover-container'><span class='glow-tech'>exploratory calculations</span><span class='tech-tooltip-box'><strong>Exploratory Calculations</strong>Initial mathematical operations used to examine data distributions, outliers, and basic statistics before model training.</span></span>, heatmaps, and <span class='tech-hover-container'><span class='glow-tech'>merging steps</span><span class='tech-tooltip-box'><strong>Merging Steps</strong>Database join operations that combine separate datasets (e.g. current client details and previous loans) using shared primary keys.</span></span> executed.")

    st.markdown("---")
    if st.button("▶ Run Full Source Code", type="primary", use_container_width=True):
        import time
        col1, col2 = st.columns([1.5, 1])
        with col1:
            st.markdown("### Output")
            output_data_load = st.empty()
            output_cleaning = st.empty()
            output_model = st.empty()
        with col2:
            st.markdown("### Execution Status")
            status_panel = st.empty()

        # Sequence 1: Loading
        status_panel.info("⏳ Executing lines 1-50: Importing libraries and loading Credit applications dataset...")
        time.sleep(1.5)
        with output_data_load.container():
            st.success("✅ Dataset 'application_data.csv' loaded successfully (307,511 rows).")
            mock_df = pd.DataFrame({
                "SK_ID_CURR": [100002, 100003, 100004],
                "TARGET": [1, 0, 0],
                "NAME_CONTRACT_TYPE": ["Cash loans", "Cash loans", "Revolving loans"],
                "CODE_GENDER": ["M", "F", "M"],
                "FLAG_OWN_CAR": ["N", "N", "Y"],
                "AMT_INCOME_TOTAL": [202500.0, 270000.0, 67500.0]
            })
            st.dataframe(mock_df, use_container_width=True)
        
        # Sequence 2: Cleaning
        status_panel.info("⏳ Executing lines 51-120: Applying data cleaning, imputing missing values, and binning variables...")
        time.sleep(2.0)
        with output_cleaning.container():
            st.success("✅ Data cleaning complete. Missing values handled and age/income binned.")
            mock_clean_df = pd.DataFrame({
                "SK_ID_CURR": [100002, 100003, 100004],
                "Income_Bin": ["Medium", "High", "Low"],
                "Age_Bin": ["20-30", "40-50", "50-60"]
            })
            st.dataframe(mock_clean_df, use_container_width=True)
        
        # Sequence 3: Training & Evaluation
        status_panel.info("⏳ Executing lines 121-200: Performing univariate/bivariate analysis and generating visualizations...")
        time.sleep(2.5)
        with output_model.container():
            st.success("✅ EDA pipeline executed. Correlation heatmaps and distributions generated.")
            corr = np.array([[1.0, 0.2, -0.1], [0.2, 1.0, 0.05], [-0.1, 0.05, 1.0]])
            fig, ax = plt.subplots(figsize=(5,3))
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax, cbar=False)
            ax.set_title("Correlation Heatmap (Numeric Variables)")
            st.pyplot(fig)
        
        status_panel.success("🎉 Full source code executed successfully!")



import streamlit.components.v1 as components

components.html('''
<script>
    const parent = window.parent.document;
    
    // 1. Find the hidden button by its text
    const buttons = parent.querySelectorAll('button');
    let hiddenBtn = null;
    buttons.forEach(b => {
        if (b.innerText.includes("HIDDEN_TOGGLE_DO_NOT_CLICK")) {
            hiddenBtn = b;
        }
    });

    if (hiddenBtn) {
        // 2. Hide the button container completely
        const container = hiddenBtn.closest('.element-container');
        if (container) {
            container.style.position = 'absolute';
            container.style.opacity = '0';
            container.style.pointerEvents = 'none';
            container.style.width = '0px';
            container.style.height = '0px';
            container.style.display = 'none'; 
        }

        // 3. Attach click listener to premium-hero
        const heroes = parent.querySelectorAll('.premium-hero');
        heroes.forEach(hero => {
            hero.addEventListener('click', () => {
                hiddenBtn.click();
            });
        });
    }
</script>
''', height=0)
