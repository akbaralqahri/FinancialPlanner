import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json

# Konfigurasi halaman
st.set_page_config(
    page_title="Financial Planner - by @akbaralqahri",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk dark mode dengan font cerah
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    /* Global Styles - DARK MODE */
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Main Background - Dark */
    .main {
        background: #0f172a;
        padding: 1.5rem;
    }
    
    .block-container {
        background: #1e293b;
        border-radius: 24px;
        padding-top: 6rem !important; /* Memberikan ruang agar tidak tertutup navbar */
        padding-bottom: 3rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        box-shadow: 0 24px 48px rgba(0,0,0,0.4);
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Headers - REDESIGNED & FIXED */
    .main-header {
        font-size: 2.5rem; /* Ukuran disesuaikan agar lebih rapi */
        font-weight: 800;
        text-align: left; /* Align left for better layout with columns */
        /* Brighter gradient for better contrast on dark bg */
        background: linear-gradient(90deg, #f8fafc 0%, #a78bfa 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        line-height: 1.2;
        filter: drop-shadow(0 0 15px rgba(167, 139, 250, 0.3));
    }
    
    .sub-header {
        font-size: 1.1rem;
        color: #94a3b8;
        text-align: left;
        margin-bottom: 2rem;
        font-weight: 500;
        letter-spacing: 0.01em;
    }
    
    /* Metric Cards - Dark with Glow */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        border: 2px solid #334155;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        min-height: 110px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(167, 139, 250, 0.3);
        border-color: #a78bfa;
        background: linear-gradient(135deg, #334155 0%, #475569 100%);
    }
    
    /* Fix Streamlit Metric Container */
    [data-testid="stMetric"] {
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
        max-width: 100% !important;
    }
    
    [data-testid="metric-container"] {
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
        max-width: 100% !important;
    }
    
    /* Ensure metric values don't overflow */
    [data-testid="stMetricValue"] {
        font-size: 1.3rem !important;
        font-weight: 800;
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2 !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        max-width: 100% !important;
        white-space: normal !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.75rem !important;
        font-weight: 600;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem !important;
        line-height: 1.3 !important;
        white-space: normal !important;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.75rem !important;
        margin-top: 0.25rem !important;
    }
    
    /* Info Boxes - Dark Variants */
    .info-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        padding: 1.5rem;
        border-radius: 16px;
        border-left: 5px solid #60a5fa;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(96, 165, 250, 0.2);
        color: #e0e7ff;
    }
    
    .success-box {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        padding: 1.5rem;
        border-radius: 16px;
        border-left: 5px solid #34d399;
        box-shadow: 0 4px 12px rgba(52, 211, 153, 0.2);
        color: #d1fae5;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #92400e 0%, #b45309 100%);
        padding: 1.5rem;
        border-radius: 16px;
        border-left: 5px solid #fbbf24;
        box-shadow: 0 4px 12px rgba(251, 191, 36, 0.2);
        color: #fef3c7;
    }
    
    /* Buttons - Bright Gradient */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: 600;
        padding: 0.875rem 1.75rem;
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        border: none;
        color: white;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 16px rgba(167, 139, 250, 0.4);
        font-size: 0.95rem;
        letter-spacing: 0.02em;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(167, 139, 250, 0.6);
        background: linear-gradient(135deg, #c4b5fd 0%, #f472b6 100%);
    }
    
    /* Sidebar - Dark Theme */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }
    
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        font-weight: 700;
    }
    
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #e2e8f0 !important;
    }
    
    /* Radio buttons in sidebar */
    [data-testid="stSidebar"] .row-widget.stRadio > div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.05);
        padding: 0.75rem 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        transition: all 0.2s ease;
        cursor: pointer;
        color: #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] .row-widget.stRadio > div[role="radiogroup"] > label:hover {
        background: rgba(167, 139, 250, 0.2);
        border-left: 3px solid #a78bfa;
    }
    
    /* Progress Bar - Neon Gradient */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%);
        border-radius: 10px;
        height: 10px;
        box-shadow: 0 0 10px rgba(167, 139, 250, 0.5);
    }
    
    .stProgress > div > div {
        background-color: #334155;
        border-radius: 10px;
        height: 10px;
    }
    
    /* Expander - Dark Design */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border-radius: 12px;
        padding: 1.25rem;
        font-weight: 600;
        color: #e2e8f0 !important;
        border: 2px solid #334155;
        transition: all 0.2s ease;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #a78bfa;
        background: linear-gradient(135deg, #334155 0%, #475569 100%);
        box-shadow: 0 0 15px rgba(167, 139, 250, 0.3);
    }
    
    /* Tabs - Dark Modern Style */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.75rem;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        padding: 0.875rem 1.75rem;
        font-weight: 600;
        background: #1e293b;
        border: 2px solid #334155;
        color: #94a3b8;
        transition: all 0.2s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: #334155;
        border-color: #475569;
        color: #e2e8f0;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        color: white !important;
        border-color: #a78bfa;
        box-shadow: 0 4px 12px rgba(167, 139, 250, 0.4);
    }
    
    /* Cards Container - Dark Shadow Elevation */
    .card {
        background: #1e293b;
        border-radius: 16px;
        padding: 1.75rem;
        border: 2px solid #334155;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 12px 24px rgba(167, 139, 250, 0.2);
        border-color: #475569;
        transform: translateY(-2px);
    }
    
    /* Health Score Badge - Dark with Glow */
    .health-badge {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        border: 3px solid;
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
    }
    
    .health-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 32px rgba(167, 139, 250, 0.3);
    }
    
    /* Input Fields - Dark Theme */
    .stNumberInput input, .stTextInput input, .stSelectbox select {
        border-radius: 12px;
        border: 2px solid #334155 !important;
        padding: 0.875rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        background: #0f172a !important;
        color: #e2e8f0 !important;
    }
    
    .stNumberInput input:focus, .stTextInput input:focus, .stSelectbox select:focus {
        border-color: #a78bfa !important;
        box-shadow: 0 0 0 4px rgba(167, 139, 250, 0.2) !important;
        background: #1e293b !important;
        outline: none;
    }
    
    /* Slider - Neon Style */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%);
    }
    
    .stSlider [role="slider"] {
        background-color: #a78bfa;
    }
    
    /* Section Divider - Elegant Dark */
    hr {
        margin: 3rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #334155 20%, #334155 80%, transparent);
    }
    
    /* Download Button - Special Dark Styling */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.875rem 1.75rem;
        font-weight: 600;
        box-shadow: 0 4px 16px rgba(5, 150, 105, 0.4);
        transition: all 0.3s ease;
    }
    
    .stDownloadButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(5, 150, 105, 0.6);
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    }
    
    /* Info/Success/Warning Streamlit Components - Dark */
    .stAlert {
        border-radius: 12px;
        border-width: 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        background: #1e293b;
        color: #e2e8f0;
    }
    
    /* DataFrame styling - Dark */
    .dataframe {
        border-radius: 12px !important;
        overflow: hidden;
        border: 2px solid #334155;
        background: #1e293b !important;
        color: #e2e8f0 !important;
    }
    
    .dataframe tbody tr:hover {
        background-color: #334155 !important;
    }
    
    .dataframe thead tr th {
        background-color: #0f172a !important;
        color: #e2e8f0 !important;
        font-weight: 600;
    }
    
    .dataframe tbody tr td {
        color: #e2e8f0 !important;
    }
    
    /* Custom scrollbar - Dark */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1e293b;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #c4b5fd 0%, #f472b6 100%);
    }
    
    /* Column spacing */
    [data-testid="column"] {
        padding: 0 0.75rem;
    }
    
    /* Remove default streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Section headers - Bright */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #e2e8f0;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 3px solid #334155;
    }
    
    /* Icon text - Bright */
    .icon-text {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #e2e8f0;
    }
    
    /* Plotly charts - Dark integration */
    .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
    }
    
    /* Text colors - Override Streamlit defaults */
    p, span, div, label {
        color: #e2e8f0;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #f1f5f9 !important;
    }
    
    /* Caption text */
    .caption, [data-testid="stCaptionContainer"] {
        color: #94a3b8 !important;
    }
    
    /* Select box - Dark */
    .stSelectbox > div > div {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    
    /* Number input controls */
    .stNumberInput button {
        background: #334155 !important;
        color: #e2e8f0 !important;
        border-color: #334155 !important;
    }
    
    .stNumberInput button:hover {
        background: #475569 !important;
    }
    
    /* Expander content */
    .streamlit-expanderContent {
        background: #1e293b;
        border: 2px solid #334155;
        border-top: none;
        border-radius: 0 0 12px 12px;
    }
    
    /* Success/Info message boxes */
    .element-container .stMarkdown .success {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        color: #d1fae5;
    }
    
    .element-container .stMarkdown .info {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        color: #e0e7ff;
    }
    
    .element-container .stMarkdown .warning {
        background: linear-gradient(135deg, #92400e 0%, #b45309 100%);
        color: #fef3c7;
    }
    
    /* Custom metric styling for HTML-based metrics */
    .custom-metric {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 1.25rem;
        border-radius: 16px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        border: 2px solid #334155;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        min-height: 100px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .custom-metric:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(167, 139, 250, 0.3);
        border-color: #a78bfa;
        background: linear-gradient(135deg, #334155 0%, #475569 100%);
    }
    
    .custom-metric-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    
    .custom-metric-value {
        font-size: 1.4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        word-wrap: break-word;
        overflow-wrap: break-word;
        line-height: 1.3;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    /* Compact variant for smaller metrics */
    .custom-metric-compact {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        border: 2px solid #334155;
        transition: all 0.3s ease;
        overflow: hidden;
    }
    
    .custom-metric-compact:hover {
        border-color: #475569;
        box-shadow: 0 8px 16px rgba(167, 139, 250, 0.2);
    }
    
    .custom-metric-compact .custom-metric-label {
        font-size: 0.7rem;
        margin-bottom: 0.4rem;
    }
    
    .custom-metric-compact .custom-metric-value {
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Fungsi utility
def format_idr(amount):
    """Format angka ke format Rupiah"""
    return f"Rp {amount:,.0f}".replace(",", ".")

def format_number(num):
    """Format angka biasa"""
    return f"{num:,.0f}".replace(",", ".")

def calculate_financial_health(data, debts, emergency_target):
    """Hitung skor kesehatan finansial"""
    score = 0
    
    # 1. Savings Rate (40 poin)
    savings_rate = ((data['monthly_income'] - data['monthly_expenses']) / data['monthly_income']) * 100
    if savings_rate >= 20:
        score += 40
    elif savings_rate >= 10:
        score += 20
    
    # 2. Debt Ratio (30 poin)
    if len(debts) > 0:
        min_debt_payment = sum([d['min_payment'] for d in debts])
        debt_ratio = (min_debt_payment / data['monthly_income']) * 100
        if debt_ratio <= 30:
            score += 30
        elif debt_ratio <= 40:
            score += 15
    else:
        score += 30
    
    # 3. Emergency Fund (30 poin)
    ef_progress = (data['current_savings'] / emergency_target) * 100
    if ef_progress >= 100:
        score += 30
    elif ef_progress >= 50:
        score += 15
    
    if score > 80:
        label = "Sangat Sehat"
        color = "#34d399"
    elif score > 50:
        label = "Cukup Sehat"
        color = "#fbbf24"
    else:
        label = "Perlu Perhatian"
        color = "#f87171"
    
    return score, label, color

def simulate_debt_payoff(debts, monthly_budget, strategy='avalanche'):
    """Simulasi pelunasan hutang"""
    if not debts or monthly_budget <= 0:
        return {'months': 0, 'interest': 0, 'timeline': []}
    
    temp_debts = [d.copy() for d in debts]
    total_interest = 0
    months = 0
    timeline = []
    
    while any(d['balance'] > 0 for d in temp_debts) and months < 360:
        months += 1
        available_budget = monthly_budget
        month_payment = 0
        
        # Bayar minimum dan bunga
        for debt in temp_debts:
            if debt['balance'] > 0:
                interest = (debt['balance'] * (debt['interest'] / 100)) / 12
                total_interest += interest
                debt['balance'] += interest
                
                payment = min(debt['balance'], debt['min_payment'])
                debt['balance'] -= payment
                available_budget -= payment
                month_payment += payment
        
        # Alokasi sisa budget
        if available_budget > 0:
            if strategy == 'snowball':
                target = sorted([d for d in temp_debts if d['balance'] > 0], 
                              key=lambda x: x['balance'])
            else:  # avalanche
                target = sorted([d for d in temp_debts if d['balance'] > 0], 
                              key=lambda x: x['interest'], reverse=True)
            
            if target:
                extra_payment = min(available_budget, target[0]['balance'])
                target[0]['balance'] -= extra_payment
                month_payment += extra_payment
        
        remaining_debt = sum(d['balance'] for d in temp_debts)
        timeline.append({
            'month': months,
            'remaining': remaining_debt,
            'payment': month_payment
        })
    
    return {
        'months': months,
        'interest': total_interest,
        'timeline': timeline
    }

def calculate_fire_projection(data, years=30):
    """Proyeksi FIRE (Financial Independence Retire Early)"""
    current = data['current_savings']
    monthly_invest = data['monthly_income'] - data['monthly_expenses']
    real_return = (data['investment_return'] - data['inflation_rate']) / 100
    
    projection = []
    for year in range(years + 1):
        projection.append({
            'year': year,
            'value': current,
            'age': data.get('age', 30) + year
        })
        current = current * (1 + real_return) + (monthly_invest * 12)
        
        fire_number = (data['monthly_expenses'] * 12) * 25
        if current > fire_number * 2:
            break
    
    return projection

# Inisialisasi session state
if 'financial_data' not in st.session_state:
    st.session_state.financial_data = {
        'monthly_income': 15000000,
        'monthly_expenses': 8000000,
        'current_savings': 50000000,
        'age': 30,
        'marital_status': 'single',
        'inflation_rate': 4.0,
        'investment_return': 8.0,
        'risk_profile': 'Moderate'
    }

if 'debts' not in st.session_state:
    st.session_state.debts = [
        {'id': 1, 'name': 'Kartu Kredit', 'balance': 15000000, 'interest': 20, 'min_payment': 1500000},
        {'id': 2, 'name': 'KTA Bank', 'balance': 30000000, 'interest': 12, 'min_payment': 1000000}
    ]

if 'debt_budget' not in st.session_state:
    st.session_state.debt_budget = 3000000

if 'goals' not in st.session_state:
    st.session_state.goals = [
        {'id': 1, 'name': 'Dana Menikah', 'target': 100000000, 'current': 20000000, 'deadline_year': 2027}
    ]

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 📊 Financial Planner")
    st.markdown("**by @akbaralqahri**")
    st.markdown("---")

    menu = st.radio(
        "Navigasi",
        ["🏠 Dashboard Utama", "💰 Budget & Alokasi", "🎯 Tujuan Keuangan", 
         "🛡️ Dana Darurat", "📉 Kalkulator Hutang", "🔥 Simulasi FIRE",
         "⚙️ Pengaturan"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### 👤 Profil Pengguna")
    st.info("**User Indonesia**\nFree Plan")

# Hitung metrik penting
data = st.session_state.financial_data
debts = st.session_state.debts
goals = st.session_state.goals

# Emergency Fund Target
ef_multipliers = {'single': 6, 'married': 9, 'married_with_kids': 12}
emergency_target = data['monthly_expenses'] * ef_multipliers[data['marital_status']]

# FIRE Number
fire_number = (data['monthly_expenses'] * 12) * 25

# Total Debt
total_debt = sum([d['balance'] for d in debts])

# Financial Health Score
health_score, health_label, health_color = calculate_financial_health(data, debts, emergency_target)

# =============================================================================
# DASHBOARD UTAMA
# =============================================================================
if menu == "🏠 Dashboard Utama":
    col_header, col_badge = st.columns([3, 1])
    
    with col_header:
        st.markdown('<p class="main-header">Ringkasan Eksekutif</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="sub-header">Selamat datang kembali! Status keuangan Anda: <strong style="color: {health_color};">{health_label}</strong></p>', unsafe_allow_html=True)
    
    with col_badge:
        st.markdown(f"""
        <div class='health-badge' style='border-color: {health_color};'>
            <div style='font-size: 0.7rem; color: {health_color}; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: 0.1em;'>HEALTH SCORE</div>
            <div style='font-size: 3rem; font-weight: 800; color: {health_color};'>{health_score}</div>
            <div style='font-size: 0.9rem; color: #94a3b8; margin-top: 0.5rem; font-weight: 600;'>{health_label}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Stats - Using HTML instead of Streamlit metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'''
        <div class="custom-metric">
            <div class="custom-metric-label">💵 Pendapatan</div>
            <div class="custom-metric-value">{format_idr(data['monthly_income'])}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'''
        <div class="custom-metric">
            <div class="custom-metric-label">💸 Pengeluaran</div>
            <div class="custom-metric-value">{format_idr(data['monthly_expenses'])}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'''
        <div class="custom-metric">
            <div class="custom-metric-label">💰 Aset Likuid</div>
            <div class="custom-metric-value">{format_idr(data['current_savings'])}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        st.markdown(f'''
        <div class="custom-metric">
            <div class="custom-metric-label">⚠️ Total Hutang</div>
            <div class="custom-metric-value">{format_idr(total_debt)}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Main Content
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # Parameter Keuangan
        st.markdown('<p class="section-header">⚙️ Parameter Keuangan Utama</p>', unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            income = st.number_input(
                "💵 Pendapatan Bulanan (Rp)",
                min_value=0,
                value=data['monthly_income'],
                step=100000,
                format="%d"
            )
            
            savings = st.number_input(
                "💰 Tabungan Saat Ini (Rp)",
                min_value=0,
                value=data['current_savings'],
                step=1000000,
                format="%d"
            )
        
        with col_b:
            expenses = st.number_input(
                "💸 Pengeluaran Bulanan (Rp)",
                min_value=0,
                value=data['monthly_expenses'],
                step=100000,
                format="%d"
            )
            
            marital = st.selectbox(
                "👥 Status Pernikahan",
                options=['single', 'married', 'married_with_kids'],
                index=['single', 'married', 'married_with_kids'].index(data['marital_status']),
                format_func=lambda x: {
                    'single': 'Lajang (Single)',
                    'married': 'Menikah',
                    'married_with_kids': 'Menikah + Anak'
                }[x]
            )
        
        # Update data
        if (income != data['monthly_income'] or expenses != data['monthly_expenses'] or 
            savings != data['current_savings'] or marital != data['marital_status']):
            st.session_state.financial_data.update({
                'monthly_income': income,
                'monthly_expenses': expenses,
                'current_savings': savings,
                'marital_status': marital
            })
            st.rerun()
        
        st.markdown("")
        
        # Rekomendasi Cerdas
        st.markdown('<p class="section-header">💡 Rekomendasi Cerdas</p>', unsafe_allow_html=True)
        if data['current_savings'] < emergency_target:
            gap = emergency_target - data['current_savings']
            st.markdown(f"""
            <div class='warning-box'>
                <div style='font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;'>⚠️ Prioritas: Dana Darurat</div>
                <div>Fokus utama Anda saat ini adalah memenuhi Dana Darurat sebesar 
                <strong>{format_idr(gap)}</strong> lagi sebelum investasi agresif.</div>
            </div>
            """, unsafe_allow_html=True)
        elif len(debts) > 0:
            st.markdown("""
            <div class='info-box'>
                <div style='font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;'>✅ Dana Darurat Aman!</div>
                <div>Sekarang alihkan cashflow untuk melunasi hutang bunga tinggi (metode Avalanche).</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='success-box'>
                <div style='font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;'>🎉 Kondisi Prima!</div>
                <div>Maksimalkan investasi bulanan untuk mempercepat FIRE.</div>
            </div>
            """, unsafe_allow_html=True)
    
    with col_right:
        # Metrik Kesehatan
        st.markdown('<p class="section-header">📊 Metrik Kesehatan</p>', unsafe_allow_html=True)
        
        # Rasio Menabung
        savings_rate = ((data['monthly_income'] - data['monthly_expenses']) / data['monthly_income']) * 100
        
        # Rasio Hutang
        if debts:
            min_debt = sum([d['min_payment'] for d in debts])
            debt_ratio = (min_debt / data['monthly_income']) * 100
        else:
            debt_ratio = 0
        
        # Dana Darurat
        ef_progress = (data['current_savings'] / emergency_target) * 100
        
        st.markdown(f'''
<div class="card">
<div style='font-weight: 600; color: #e2e8f0; margin-bottom: 0.5rem;'>💰 Rasio Menabung: {savings_rate:.1f}%</div>
<div style='background-color: #334155; border-radius: 10px; height: 10px; margin-bottom: 0.5rem; overflow: hidden;'>
<div style='background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%); height: 100%; width: {min(savings_rate / 20 * 100, 100)}%; border-radius: 10px; transition: width 0.3s ease;'></div>
</div>
<div style='font-size: 0.75rem; color: #94a3b8; margin-bottom: 1.5rem;'>Target ideal: >20%</div>
<div style='font-weight: 600; color: #e2e8f0; margin-bottom: 0.5rem;'>💳 Rasio Hutang: {debt_ratio:.1f}%</div>
<div style='background-color: #334155; border-radius: 10px; height: 10px; margin-bottom: 0.5rem; overflow: hidden;'>
<div style='background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%); height: 100%; width: {min(debt_ratio / 30 * 100, 100)}%; border-radius: 10px; transition: width 0.3s ease;'></div>
</div>
<div style='font-size: 0.75rem; color: #94a3b8; margin-bottom: 1.5rem;'>Target maksimal: <30%</div>
<div style='font-weight: 600; color: #e2e8f0; margin-bottom: 0.5rem;'>🛡️ Dana Darurat: {ef_progress:.1f}%</div>
<div style='background-color: #334155; border-radius: 10px; height: 10px; margin-bottom: 0.5rem; overflow: hidden;'>
<div style='background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%); height: 100%; width: {min(ef_progress, 100)}%; border-radius: 10px; transition: width 0.3s ease;'></div>
</div>
<div style='font-size: 0.75rem; color: #94a3b8;'>Target: {format_idr(emergency_target)}</div>
</div>
''', unsafe_allow_html=True)
    
    # Cashflow Chart
    st.markdown("---")
    st.markdown('<p class="section-header">💵 Analisis Cashflow Bulanan</p>', unsafe_allow_html=True)
    
    cashflow_data = {
        'Kategori': ['Pendapatan', 'Pengeluaran', 'Tabungan'],
        'Jumlah': [data['monthly_income'], data['monthly_expenses'], 
                   data['monthly_income'] - data['monthly_expenses']],
        'Tipe': ['Masuk', 'Keluar', 'Sisa']
    }
    
    fig = px.bar(
        cashflow_data,
        x='Kategori',
        y='Jumlah',
        color='Tipe',
        color_discrete_map={'Masuk': '#34d399', 'Keluar': '#f87171', 'Sisa': '#a78bfa'},
        text='Jumlah'
    )
    
    fig.update_traces(
        texttemplate='Rp %{text:,.0f}', 
        textposition='outside',
        marker_line_color='#0f172a',
        marker_line_width=2
    )
    fig.update_layout(
        showlegend=False,
        height=450,
        yaxis_title="Jumlah (Rp)",
        xaxis_title="",
        plot_bgcolor='#1e293b',
        paper_bgcolor='#1e293b',
        font=dict(family='Plus Jakarta Sans', size=13, color='#e2e8f0'),
        margin=dict(t=20, b=20, l=20, r=20),
        yaxis=dict(gridcolor='#334155', zerolinecolor='#334155'),
        xaxis=dict(gridcolor='#334155')
    )
    
    st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# BUDGET & ALOKASI
# =============================================================================
elif menu == "💰 Budget & Alokasi":
    st.markdown('<p class="main-header">Manajemen Anggaran</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Kelola aset dan masa depan Anda dengan metode terbukti</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        allocations_503020 = [
            {'label': 'Kebutuhan (Needs)', 'pct': 50, 'color': '#f87171', 'desc': 'Sewa, Makan, Listrik, Transportasi', 'icon': '🏠'},
            {'label': 'Keinginan (Wants)', 'pct': 30, 'color': '#fbbf24', 'desc': 'Hobi, Hiburan, Belanja Non-Esensial', 'icon': '🎮'},
            {'label': 'Tabungan (Savings)', 'pct': 20, 'color': '#34d399', 'desc': 'Investasi, Dana Darurat, Pensiun', 'icon': '💎'}
        ]
        
        html_content = '''
<div class="card">
<div style='font-size: 1.5rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.5rem;'>📊 50/30/20 Rule</div>
<div style='font-size: 0.875rem; color: #94a3b8; margin-bottom: 1.5rem;'>Metode klasik yang seimbang dan mudah diterapkan</div>
'''
        
        for item in allocations_503020:
            amount = data['monthly_income'] * (item['pct'] / 100)
            html_content += f'''
<div style='margin-top: 1.25rem;'>
<div style='font-weight: 700; font-size: 1rem; color: #e2e8f0; margin-bottom: 0.5rem;'>{item['icon']} {item['label']}</div>
<div style='color: {item['color']}; font-weight: 700; font-size: 1.2rem; margin: 0.4rem 0; line-height: 1.3;'>
{format_idr(amount)} <span style='font-size: 0.9rem; opacity: 0.8;'>({item['pct']}%)</span>
</div>
<div style='font-size: 0.75rem; color: #94a3b8; margin-bottom: 0.5rem;'>{item['desc']}</div>
<div style='background-color: #334155; border-radius: 10px; height: 10px; overflow: hidden;'>
<div style='background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%); height: 100%; width: {item['pct']}%; border-radius: 10px;'></div>
</div>
</div>
'''
        
        html_content += '</div>'
        st.markdown(html_content, unsafe_allow_html=True)
    
    with col2:
        allocations_6jars = [
            {'label': 'Living (NEC)', 'pct': 55, 'desc': 'Biaya Hidup Rutin', 'icon': '🏠', 'color': '#60a5fa'},
            {'label': 'Freedom (FFA)', 'pct': 10, 'desc': 'Investasi Pasif', 'icon': '🗽', 'color': '#a78bfa'},
            {'label': 'Education (EDU)', 'pct': 10, 'desc': 'Buku, Kursus, Skill', 'icon': '📚', 'color': '#c084fc'},
            {'label': 'Long Term (LTSS)', 'pct': 10, 'desc': 'Gadget, Liburan Besar', 'icon': '🎯', 'color': '#f472b6'},
            {'label': 'Play', 'pct': 10, 'desc': 'Bersenang-senang', 'icon': '🎉', 'color': '#fbbf24'},
            {'label': 'Give', 'pct': 5, 'desc': 'Amal & Sosial', 'icon': '❤️', 'color': '#34d399'}
        ]
        
        html_content = '''
<div class="card">
<div style='font-size: 1.5rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.5rem;'>🏺 6 Jars System</div>
<div style='font-size: 0.875rem; color: #94a3b8; margin-bottom: 1.5rem;'>Metode T. Harv Eker untuk manajemen presisi</div>
'''
        
        for item in allocations_6jars:
            amount = data['monthly_income'] * (item['pct'] / 100)
            html_content += f'''
<div style='margin-top: 1.25rem;'>
<div style='font-weight: 700; font-size: 1rem; color: #e2e8f0; margin-bottom: 0.5rem;'>{item['icon']} {item['label']}</div>
<div style='color: {item['color']}; font-weight: 700; font-size: 1.2rem; margin: 0.4rem 0; line-height: 1.3;'>
{format_idr(amount)} <span style='font-size: 0.9rem; opacity: 0.8;'>({item['pct']}%)</span>
</div>
<div style='font-size: 0.75rem; color: #94a3b8; margin-bottom: 0.5rem;'>{item['desc']}</div>
<div style='background-color: #334155; border-radius: 10px; height: 10px; overflow: hidden;'>
<div style='background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%); height: 100%; width: {item['pct']}%; border-radius: 10px;'></div>
</div>
</div>
'''
        
        html_content += '</div>'
        st.markdown(html_content, unsafe_allow_html=True)
    
    # Tips Anggaran
    st.markdown("---")
    st.markdown('<p class="section-header">💡 Tips Anggaran Praktis</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **🧮 Catat Pengeluaran**
        
        Gunakan aplikasi pencatat uang setiap hari agar sadar kemana uang pergi. Konsistensi adalah kunci!
        """)
    
    with col2:
        st.info("""
        **🎯 Pay Yourself First**
        
        Sisihkan tabungan/investasi begitu gaji masuk, bukan menunggu sisa akhir bulan.
        """)
    
    with col3:
        st.info("""
        **📅 Review Bulanan**
        
        Evaluasi budget vs realisasi setiap akhir bulan untuk perbaikan berkelanjutan.
        """)

# =============================================================================
# TUJUAN KEUANGAN
# =============================================================================
elif menu == "🎯 Tujuan Keuangan":
    st.markdown('<p class="main-header">Tujuan & Mimpi</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Rencanakan dan raih impian finansial Anda</p>', unsafe_allow_html=True)
    
    col_main, col_calc = st.columns([2, 1])
    
    with col_main:
        st.markdown('<p class="section-header">📋 Daftar Tujuan</p>', unsafe_allow_html=True)
        
        # Loop dengan enumerasi untuk update/delete
        for idx, goal in enumerate(goals):
            # Kalkulasi progress bar
            progress = (goal['current'] / goal['target']) * 100 if goal['target'] > 0 else 0
            
            years_left = goal['deadline_year'] - datetime.now().year
            months_left = max(years_left * 12, 1)
            gap = goal['target'] - goal['current']
            monthly_needed = gap / months_left if months_left > 0 else gap

            # Menggunakan expander seperti kalkulator hutang
            with st.expander(f"🎯 {goal['name']} ({progress:.1f}%)", expanded=False):
                # Visualisasi mini di dalam expander
                col_viz_1, col_viz_2 = st.columns([3, 1])
                with col_viz_1:
                    st.progress(min(progress / 100, 1.0))
                    st.caption(f"Terkumpul: {format_idr(goal['current'])} dari {format_idr(goal['target'])}")
                with col_viz_2:
                    st.markdown(f"<div style='text-align:right; font-weight:bold; color:#a78bfa;'>{format_idr(monthly_needed)}/bln</div>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Form Edit
                col_a, col_b = st.columns(2)
                
                with col_a:
                    new_name = st.text_input(
                        "📝 Nama Tujuan",
                        value=goal['name'],
                        key=f"goal_name_{goal['id']}"
                    )
                    
                    new_current = st.number_input(
                        "💰 Dana Terkumpul (Rp)",
                        min_value=0,
                        value=goal['current'],
                        step=1000000,
                        key=f"goal_current_{goal['id']}",
                        format="%d"
                    )
                
                with col_b:
                    new_target = st.number_input(
                        "🎯 Target Dana (Rp)",
                        min_value=0,
                        value=goal['target'],
                        step=1000000,
                        key=f"goal_target_{goal['id']}",
                        format="%d"
                    )
                    
                    new_year = st.number_input(
                        "📅 Tahun Target",
                        min_value=datetime.now().year,
                        value=goal['deadline_year'],
                        step=1,
                        key=f"goal_year_{goal['id']}"
                    )
                
                # Tombol Aksi
                col_update, col_delete = st.columns([3, 1])
                
                with col_update:
                    if st.button(f"💾 Update", key=f"update_goal_{goal['id']}", use_container_width=True):
                        st.session_state.goals[idx].update({
                            'name': new_name,
                            'current': new_current,
                            'target': new_target,
                            'deadline_year': new_year
                        })
                        st.rerun()
                
                with col_delete:
                    if st.button(f"🗑️", key=f"delete_goal_{goal['id']}", use_container_width=True):
                        st.session_state.goals.pop(idx)
                        st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Tombol Tambah Goal
        if st.button("➕ Tambah Tujuan Baru", use_container_width=True):
            new_goal = {
                'id': max([g['id'] for g in goals]) + 1 if goals else 1,
                'name': 'Tujuan Baru',
                'target': 10000000,
                'current': 0,
                'deadline_year': datetime.now().year + 5
            }
            st.session_state.goals.append(new_goal)
            st.rerun()
    
    with col_calc:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<div style='font-size: 1.3rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.5rem;'>🧮 Kalkulator Cepat</div>", unsafe_allow_html=True)
        st.caption("Hitung kebutuhan menabung dengan mudah")
        
        st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
        
        calc_target = st.number_input(
            "🎯 Target Dana (Rp)",
            min_value=0,
            value=100000000,
            step=10000000,
            format="%d"
        )
        
        calc_year = st.number_input(
            "📅 Tahun Tercapai",
            min_value=datetime.now().year,
            value=datetime.now().year + 5,
            step=1
        )
        
        calc_current = st.number_input(
            "💰 Dana Tersedia (Rp)",
            min_value=0,
            value=0,
            step=1000000,
            format="%d"
        )
        
        years_to_goal = calc_year - datetime.now().year
        months_to_goal = max(years_to_goal * 12, 1)
        gap_to_goal = calc_target - calc_current
        monthly_to_goal = gap_to_goal / months_to_goal
        
        st.markdown("---")
        st.markdown(f"""
        <div class="custom-metric-compact" style="text-align: center;">
            <div class="custom-metric-label">✨ Hasil Perhitungan</div>
            <div class="custom-metric-value" style="color: #34d399;">{format_idr(monthly_to_goal)}</div>
            <div style="font-size: 0.7rem; color: #94a3b8; margin-top: 0.4rem;">per bulan x {years_to_goal} tahun</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# DANA DARURAT
# =============================================================================
elif menu == "🛡️ Dana Darurat":
    st.markdown('<p class="main-header">Dana Darurat</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Pelindung keuangan Anda dari ketidakpastian</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Progress Circle
        ef_progress = min((data['current_savings'] / emergency_target) * 100, 100)
        
        html_content = f'''
        <div class="card">
            <div style='font-size: 1.5rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>🎯 Status Dana Darurat</div>
        '''
        
        st.markdown(html_content, unsafe_allow_html=True)
        
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=ef_progress,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Kesiapan Dana Darurat (%)", 'font': {'size': 18, 'family': 'Plus Jakarta Sans', 'color': '#e2e8f0'}},
            delta={'reference': 100, 'increasing': {'color': "#34d399"}},
            number={'font': {'size': 48, 'family': 'Plus Jakarta Sans', 'color': '#e2e8f0'}},
            gauge={
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#64748b"},
                'bar': {'color': "#34d399" if ef_progress >= 100 else "#fbbf24"},
                'bgcolor': "#1e293b",
                'borderwidth': 3,
                'bordercolor': "#334155",
                'steps': [
                    {'range': [0, 50], 'color': '#450a0a'},
                    {'range': [50, 100], 'color': '#713f12'}
                ],
                'threshold': {
                    'line': {'color': "#34d399", 'width': 4},
                    'thickness': 0.75,
                    'value': 100
                }
            }
        ))
        
        fig.update_layout(
            height=350,
            font=dict(family='Plus Jakarta Sans', color='#e2e8f0'),
            paper_bgcolor='#1e293b',
            plot_bgcolor='#1e293b',
            margin=dict(t=40, b=20, l=20, r=20)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f'''
            <div class="custom-metric-compact">
                <div class="custom-metric-label">💰 Dana Terkumpul</div>
                <div class="custom-metric-value">{format_idr(data['current_savings'])}</div>
            </div>
            ''', unsafe_allow_html=True)
        with col_b:
            st.markdown(f'''
            <div class="custom-metric-compact">
                <div class="custom-metric-label">🎯 Target</div>
                <div class="custom-metric-value">{format_idr(emergency_target)}</div>
            </div>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        allocations = [
            {'label': 'Tabungan Bank (ATM)', 'pct': 30, 'icon': '🏦', 
             'desc': 'Akses instan untuk keadaan darurat (sakit mendadak, dll)', 'color': '#60a5fa'},
            {'label': 'Reksadana Pasar Uang', 'pct': 50, 'icon': '📈', 
             'desc': 'Bunga lebih tinggi dari bank, cair dalam 1-2 hari kerja', 'color': '#a78bfa'},
            {'label': 'Emas / Cash Tunai', 'pct': 20, 'icon': '💰', 
             'desc': 'Lindung nilai inflasi dan cadangan jangka panjang', 'color': '#fbbf24'}
        ]
        
        html_content = '''
<div class="card">
<div style='font-size: 1.5rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>💼 Alokasi Penyimpanan</div>
<div style='font-size: 0.875rem; color: #94a3b8; margin-bottom: 1.5rem;'>Diversifikasi untuk keamanan dan likuiditas optimal</div>
'''
        
        for item in allocations:
            amount = data['current_savings'] * (item['pct'] / 100)
            html_content += f'''
<div style='margin-top: 1.25rem;'>
<div style='font-weight: 700; font-size: 1rem; color: #e2e8f0; margin-bottom: 0.5rem;'>{item['icon']} {item['label']}</div>
<div style='color: {item['color']}; font-weight: 700; font-size: 1.2rem; margin: 0.4rem 0; line-height: 1.3;'>
{format_idr(amount)} <span style='font-size: 0.9rem; opacity: 0.8;'>({item['pct']}%)</span>
</div>
<div style='font-size: 0.75rem; color: #94a3b8; margin-bottom: 0.5rem;'>{item['desc']}</div>
<div style='background-color: #334155; border-radius: 10px; height: 10px; overflow: hidden;'>
<div style='background: linear-gradient(90deg, #a78bfa 0%, #ec4899 100%); height: 100%; width: {item['pct']}%; border-radius: 10px;'></div>
</div>
</div>
'''
        
        html_content += '</div>'
        st.markdown(html_content, unsafe_allow_html=True)
    
    # Info Box
    st.markdown("---")
    st.info("""
    ### 📚 Mengapa Dana Darurat Penting?
    
    Dana darurat adalah fondasi keuangan yang kokoh. Tanpa dana darurat, kejadian tak terduga 
    seperti PHK, sakit, atau kerusakan kendaraan bisa menghancurkan rencana keuangan Anda.
    
    **Rekomendasi jumlah berdasarkan kondisi:**
    - 🧑 **Lajang**: 6 bulan pengeluaran (fleksibilitas lebih tinggi)
    - 💑 **Menikah**: 9 bulan pengeluaran (tanggung jawab bersama)
    - 👨‍👩‍👧‍👦 **Menikah + Anak**: 12 bulan pengeluaran (keamanan maksimal)
    """)

# =============================================================================
# KALKULATOR HUTANG
# =============================================================================
elif menu == "📉 Kalkulator Hutang":
    st.markdown('<p class="main-header">Strategi Bebas Hutang</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Kelola dan lunasi hutang dengan strategi terukur</p>', unsafe_allow_html=True)
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown('<p class="section-header">📋 Daftar Hutang</p>', unsafe_allow_html=True)
        
        # Display and edit debts
        for idx, debt in enumerate(debts):
            with st.expander(f"💳 {debt['name']} - {format_idr(debt['balance'])}", expanded=True):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    new_name = st.text_input(
                        "📝 Nama Hutang",
                        value=debt['name'],
                        key=f"debt_name_{debt['id']}"
                    )
                    
                    new_balance = st.number_input(
                        "💰 Sisa Pokok (Rp)",
                        min_value=0,
                        value=debt['balance'],
                        step=100000,
                        key=f"debt_balance_{debt['id']}",
                        format="%d"
                    )
                
                with col_b:
                    new_interest = st.number_input(
                        "📊 Bunga (%/tahun)",
                        min_value=0.0,
                        value=float(debt['interest']),
                        step=0.5,
                        key=f"debt_interest_{debt['id']}"
                    )
                    
                    new_min = st.number_input(
                        "💵 Pembayaran Minimum (Rp)",
                        min_value=0,
                        value=debt['min_payment'],
                        step=50000,
                        key=f"debt_min_{debt['id']}",
                        format="%d"
                    )
                
                col_update, col_delete = st.columns([3, 1])
                
                with col_update:
                    if st.button(f"💾 Update", key=f"update_{debt['id']}", use_container_width=True):
                        st.session_state.debts[idx].update({
                            'name': new_name,
                            'balance': new_balance,
                            'interest': new_interest,
                            'min_payment': new_min
                        })
                        st.rerun()
                
                with col_delete:
                    if st.button(f"🗑️", key=f"delete_{debt['id']}", use_container_width=True):
                        st.session_state.debts.pop(idx)
                        st.rerun()
        
        # Add new debt
        if st.button("➕ Tambah Hutang Baru", use_container_width=True):
            new_debt = {
                'id': max([d['id'] for d in debts]) + 1 if debts else 1,
                'name': 'Hutang Baru',
                'balance': 1000000,
                'interest': 10,
                'min_payment': 100000
            }
            st.session_state.debts.append(new_debt)
            st.rerun()
        
        # Budget setting
        st.markdown("---")
        st.markdown('<p class="section-header">💰 Budget Pelunasan Bulanan</p>', unsafe_allow_html=True)
        
        new_budget = st.number_input(
            "💵 Alokasi bulanan untuk bayar hutang (Rp)",
            min_value=0,
            value=st.session_state.debt_budget,
            step=100000,
            format="%d",
            help="Semakin besar alokasi, semakin cepat hutang lunas"
        )
        
        if new_budget != st.session_state.debt_budget:
            st.session_state.debt_budget = new_budget
            st.rerun()
    
    with col_right:
        if debts and st.session_state.debt_budget > 0:
            # Snowball simulation
            snowball = simulate_debt_payoff(debts, st.session_state.debt_budget, 'snowball')
            
            # Avalanche simulation
            avalanche = simulate_debt_payoff(debts, st.session_state.debt_budget, 'avalanche')
            
            is_winner = avalanche['interest'] < snowball['interest']
            saving = snowball['interest'] - avalanche['interest']
            
            html_content = f'''
<div class="card">
<div style='font-size: 1.3rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>🧮 Hasil Simulasi</div>
<div style='background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 1.25rem; border-radius: 12px; margin-bottom: 1rem; border: 2px solid #475569;'>
<div style='font-weight: 700; color: #e2e8f0; margin-bottom: 0.75rem;'>❄️ Snowball Method</div>
<div style='font-size: 0.75rem; color: #94a3b8; margin-bottom: 1rem;'>Bayar hutang terkecil dulu untuk motivasi psikologis</div>
<div style='display: flex; gap: 1rem; margin-top: 1rem;'>
<div style='flex: 1; background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 1rem; border-radius: 12px; border: 2px solid #334155;'>
<div style='font-size: 0.7rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-bottom: 0.4rem;'>⏱️ WAKTU</div>
<div style='font-size: 1.2rem; font-weight: 800; background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{snowball['months'] / 12:.1f} thn</div>
</div>
<div style='flex: 1; background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 1rem; border-radius: 12px; border: 2px solid #334155;'>
<div style='font-size: 0.7rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-bottom: 0.4rem;'>💸 TOTAL BUNGA</div>
<div style='font-size: 1rem; font-weight: 800; background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{format_idr(snowball['interest'])}</div>
</div>
</div>
</div>
'''
            
            if is_winner:
                html_content += '<div style="background: linear-gradient(135deg, #065f46 0%, #047857 100%); color: #d1fae5; padding: 0.75rem 1rem; border-radius: 8px; margin-bottom: 1rem; font-weight: 600; font-size: 0.9rem; text-align: center;">✅ REKOMENDASI - PALING HEMAT</div>'
            
            border_color = "#34d399" if is_winner else "#475569"
            delta_html = f'<div style="color: #34d399; font-size: 0.75rem; margin-top: 0.25rem;">-{format_idr(saving)}</div>' if is_winner and saving > 0 else ''
            
            html_content += f'''
<div style='background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 1.25rem; border-radius: 12px; border: 2px solid {border_color};'>
<div style='font-weight: 700; color: #e2e8f0; margin-bottom: 0.75rem;'>🔥 Avalanche Method</div>
<div style='font-size: 0.75rem; color: #94a3b8; margin-bottom: 1rem;'>Bayar bunga terbesar dulu - Paling efisien secara matematis</div>
<div style='display: flex; gap: 1rem; margin-top: 1rem;'>
<div style='flex: 1; background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 1rem; border-radius: 12px; border: 2px solid #334155;'>
<div style='font-size: 0.7rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-bottom: 0.4rem;'>⏱️ WAKTU</div>
<div style='font-size: 1.2rem; font-weight: 800; background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{avalanche['months'] / 12:.1f} thn</div>
</div>
<div style='flex: 1; background: linear-gradient(135deg, #1e293b 0%, #334155 100%); padding: 1rem; border-radius: 12px; border: 2px solid #334155;'>
<div style='font-size: 0.7rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-bottom: 0.4rem;'>💸 TOTAL BUNGA</div>
<div style='font-size: 1rem; font-weight: 800; background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{format_idr(avalanche['interest'])}</div>
{delta_html}
</div>
</div>
</div>
</div>
'''
            
            st.markdown(html_content, unsafe_allow_html=True)
            
            # Comparison chart
            st.markdown("---")
            st.markdown('<p class="section-header">📊 Perbandingan Timeline</p>', unsafe_allow_html=True)
            
            if snowball['timeline'] and avalanche['timeline']:
                df_snowball = pd.DataFrame(snowball['timeline'])
                df_avalanche = pd.DataFrame(avalanche['timeline'])
                
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=df_snowball['month'],
                    y=df_snowball['remaining'],
                    name='Snowball',
                    line=dict(color='#60a5fa', width=3),
                    fill='tonexty',
                    fillcolor='rgba(96, 165, 250, 0.1)'
                ))
                
                fig.add_trace(go.Scatter(
                    x=df_avalanche['month'],
                    y=df_avalanche['remaining'],
                    name='Avalanche',
                    line=dict(color='#34d399', width=3),
                    fillcolor='rgba(52, 211, 153, 0.1)'
                ))
                
                fig.update_layout(
                    title="Proyeksi Sisa Hutang dari Waktu ke Waktu",
                    xaxis_title="Bulan ke-",
                    yaxis_title="Sisa Hutang (Rp)",
                    hovermode='x unified',
                    height=350,
                    font=dict(family='Plus Jakarta Sans', color='#e2e8f0'),
                    plot_bgcolor='#1e293b',
                    paper_bgcolor='#1e293b',
                    margin=dict(t=40, b=20, l=20, r=20),
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                    ),
                    yaxis=dict(gridcolor='#334155'),
                    xaxis=dict(gridcolor='#334155')
                )
                
                st.plotly_chart(fig, use_container_width=True)
        else:
            html_content = '''
<div class="card">
<div style='font-size: 1.3rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>🧮 Hasil Simulasi</div>
'''
            
            if not debts:
                html_content += '''
<div style='background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%); color: #e0e7ff; padding: 1.5rem; border-radius: 12px; text-align: center;'>
<div style='font-size: 2rem; margin-bottom: 0.5rem;'>📋</div>
<div style='font-weight: 600;'>Tambahkan hutang untuk melihat simulasi</div>
</div>
'''
            else:
                html_content += '''
<div style='background: linear-gradient(135deg, #92400e 0%, #b45309 100%); color: #fef3c7; padding: 1.5rem; border-radius: 12px; text-align: center;'>
<div style='font-size: 2rem; margin-bottom: 0.5rem;'>💰</div>
<div style='font-weight: 600;'>Tetapkan budget pelunasan bulanan untuk melihat simulasi</div>
</div>
'''
            
            html_content += '</div>'
            st.markdown(html_content, unsafe_allow_html=True)

# =============================================================================
# SIMULASI FIRE
# =============================================================================
elif menu == "🔥 Simulasi FIRE":
    st.markdown('<p class="main-header">Peta Jalan Pensiun Dini</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Financial Independence Retire Early - Kebebasan Finansial</p>', unsafe_allow_html=True)
    
    # Header Info
    monthly_invest = data['monthly_income'] - data['monthly_expenses']
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class='card'>
        <div style='font-size: 1.3rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>🔥 Menuju Kebebasan Finansial</div>
        <p style='color: #94a3b8; line-height: 1.7;'>
        Dengan menabung <strong style='color: #a78bfa;'>{format_idr(monthly_invest)}</strong> per bulan dan asumsi return 
        investasi <strong style='color: #a78bfa;'>{data['investment_return']}%</strong> per tahun, berikut adalah proyeksi pertumbuhan aset Anda menuju kebebasan finansial.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'''
        <div class="custom-metric-compact">
            <div class="custom-metric-label">🎯 Target FIRE</div>
            <div class="custom-metric-value">{format_idr(fire_number)}</div>
            <div style="font-size: 0.7rem; color: #94a3b8; margin-top: 0.4rem;">Berbasis pengeluaran saat ini</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Projection Chart
    projection = calculate_fire_projection(data, years=30)
    df_fire = pd.DataFrame(projection)
    
    fig = go.Figure()
    
    # Area chart
    fig.add_trace(go.Scatter(
        x=df_fire['year'],
        y=df_fire['value'],
        fill='tozeroy',
        name='Proyeksi Aset',
        line=dict(color='#a78bfa', width=4),
        fillcolor='rgba(167, 139, 250, 0.2)'
    ))
    
    # Target line
    fig.add_hline(
        y=fire_number,
        line_dash="dash",
        line_color="#34d399",
        line_width=3,
        annotation_text=f"🎯 Target FIRE: {format_idr(fire_number)}",
        annotation_position="top right",
        annotation=dict(
            font=dict(size=13, color="#34d399", family="Plus Jakarta Sans"),
            bgcolor="rgba(52, 211, 153, 0.1)",
            bordercolor="#34d399",
            borderwidth=2
        )
    )
    
    fig.update_layout(
        title="Proyeksi Pertumbuhan Aset Menuju FIRE",
        xaxis_title="Tahun ke-",
        yaxis_title="Total Aset (Rp)",
        hovermode='x unified',
        height=500,
        showlegend=True,
        font=dict(family='Plus Jakarta Sans', color='#e2e8f0'),
        plot_bgcolor='#1e293b',
        paper_bgcolor='#1e293b',
        margin=dict(t=60, b=40, l=20, r=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        yaxis=dict(gridcolor='#334155'),
        xaxis=dict(gridcolor='#334155')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Parameters
    st.markdown("---")
    st.markdown('<p class="section-header">⚙️ Parameter Simulasi</p>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        inflation = st.number_input(
            "📉 Asumsi Inflasi (%)",
            min_value=0.0,
            value=data['inflation_rate'],
            step=0.1,
            help="Rata-rata inflasi Indonesia: 2-6% per tahun"
        )
    
    with col2:
        returns = st.number_input(
            "📈 Return Investasi (%)",
            min_value=0.0,
            value=data['investment_return'],
            step=0.1,
            help="Return historis saham: 8-15% per tahun"
        )
    
    with col3:
        st.markdown(f'''
        <div class="custom-metric-compact">
            <div class="custom-metric-label">🎯 Safe Withdrawal</div>
            <div class="custom-metric-value">4% Rule</div>
            <div style="font-size: 0.7rem; color: #94a3b8; margin-top: 0.4rem;">Standar industri</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        monthly_passive = (fire_number * 0.04) / 12
        st.markdown(f'''
        <div class="custom-metric-compact">
            <div class="custom-metric-label">💰 Gaji Pasif</div>
            <div class="custom-metric-value">{format_idr(monthly_passive)}</div>
            <div style="font-size: 0.7rem; color: #94a3b8; margin-top: 0.4rem;">Per bulan saat FIRE</div>
        </div>
        ''', unsafe_allow_html=True)
    
    if inflation != data['inflation_rate'] or returns != data['investment_return']:
        st.session_state.financial_data.update({
            'inflation_rate': inflation,
            'investment_return': returns
        })
        st.rerun()
    
    # Info
    st.markdown("---")
    st.info("""
    ### 📚 Apa itu FIRE (Financial Independence Retire Early)?
    
    FIRE adalah gerakan gaya hidup untuk mencapai kebebasan finansial dan pensiun dini dengan cara:
    
    1. **💪 Hemat & Investasi Agresif** - Tingkatkan savings rate hingga 50-70% dari pendapatan
    2. **🎯 Target 25x Pengeluaran** - Akumulasi aset senilai 25x dari pengeluaran tahunan Anda
    3. **📊 4% Withdrawal Rule** - Tarik 4% per tahun dari total aset untuk biaya hidup
    
    **Dengan formula ini, Anda bisa pensiun lebih awal tanpa khawatir kehabisan uang!**
    
    *Contoh: Jika pengeluaran bulanan Anda Rp 10 juta, maka FIRE number = Rp 10 juta × 12 bulan × 25 = Rp 3 miliar*
    """)

# =============================================================================
# PENGATURAN
# =============================================================================
elif menu == "⚙️ Pengaturan":
    st.markdown('<p class="main-header">Pengaturan Aplikasi</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Kelola data dan preferensi Anda</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["👤 Profil Pengguna", "💾 Manajemen Data", "📊 Parameter Advanced"])
    
    with tab1:
        st.markdown('<p class="section-header">👤 Informasi Profil</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input(
                "🎂 Usia Saat Ini",
                min_value=18,
                max_value=100,
                value=data.get('age', 30),
                help="Usia Anda saat ini untuk perhitungan proyeksi FIRE"
            )
            
            risk = st.selectbox(
                "📊 Profil Risiko Investasi",
                options=['Conservative', 'Moderate', 'Aggressive'],
                index=['Conservative', 'Moderate', 'Aggressive'].index(data['risk_profile']),
                help="Profil risiko untuk rekomendasi investasi"
            )
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<div style='font-weight: 600; color: #94a3b8; margin-bottom: 0.5rem;'>👥 Status Pernikahan:</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 1.2rem; color: #e2e8f0; font-weight: 600;'>{data['marital_status'].replace('_', ' ').title()}</div>", unsafe_allow_html=True)
            
            st.markdown("<div style='margin: 1rem 0;'></div>", unsafe_allow_html=True)
            
            st.markdown("<div style='font-weight: 600; color: #94a3b8; margin-bottom: 0.5rem;'>💪 Health Score:</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 1.2rem; color: {health_color}; font-weight: 700;'>{health_score}/100 - {health_label}</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("💾 Simpan Perubahan Profil", use_container_width=True):
            st.session_state.financial_data.update({
                'age': age,
                'risk_profile': risk
            })
            st.success("✅ Profil berhasil diperbarui!")
            st.rerun()
    
    with tab2:
        st.markdown('<p class="section-header">💾 Manajemen Data</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<div style='font-size: 1.2rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>📥 Export Data</div>", unsafe_allow_html=True)
            st.caption("Backup semua data keuangan Anda ke file JSON")
            
            export_data = {
                'financial_data': st.session_state.financial_data,
                'debts': st.session_state.debts,
                'goals': st.session_state.goals,
                'debt_budget': st.session_state.debt_budget,
                'export_date': datetime.now().isoformat(),
                'version': '1.0'
            }
            
            json_data = json.dumps(export_data, indent=2)
            
            st.download_button(
                label="📥 Download Data (JSON)",
                data=json_data,
                file_name=f"financia_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<div style='font-size: 1.2rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>🗑️ Reset Data</div>", unsafe_allow_html=True)
            st.caption("Hapus semua data dan kembalikan ke default")
            
            if st.button("⚠️ Reset Semua Data", type="secondary", use_container_width=True):
                st.warning("⚠️ Fitur reset akan menghapus semua data. Pastikan sudah backup terlebih dahulu!")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown('<p class="section-header">📊 Ringkasan Data</p>', unsafe_allow_html=True)
        
        summary_df = pd.DataFrame({
            'Metrik': [
                'Total Pendapatan Bulanan',
                'Total Pengeluaran Bulanan',
                'Total Tabungan/Aset',
                'Total Hutang',
                'Jumlah Tujuan Keuangan',
                'Skor Kesehatan Finansial'
            ],
            'Nilai': [
                format_idr(data['monthly_income']),
                format_idr(data['monthly_expenses']),
                format_idr(data['current_savings']),
                format_idr(total_debt),
                len(goals),
                f"{health_score}/100 ({health_label})"
            ]
        })
        
        st.dataframe(
            summary_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Metrik": st.column_config.TextColumn("Metrik", width="medium"),
                "Nilai": st.column_config.TextColumn("Nilai", width="medium")
            }
        )
    
    with tab3:
        st.markdown('<p class="section-header">📊 Parameter Advanced</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<div style='font-size: 1.2rem; font-weight: 700; color: #e2e8f0; margin-bottom: 1rem;'>💹 Asumsi Investasi</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            new_inflation = st.slider(
                "📉 Inflasi Tahunan (%)",
                min_value=0.0,
                max_value=15.0,
                value=data['inflation_rate'],
                step=0.1,
                help="Asumsi inflasi rata-rata per tahun"
            )
        
        with col2:
            new_returns = st.slider(
                "📈 Return Investasi Tahunan (%)",
                min_value=0.0,
                max_value=30.0,
                value=data['investment_return'],
                step=0.1,
                help="Asumsi return investasi rata-rata per tahun"
            )
        
        if st.button("💾 Update Parameter", use_container_width=True):
            st.session_state.financial_data.update({
                'inflation_rate': new_inflation,
                'investment_return': new_returns
            })
            st.success("✅ Parameter berhasil diperbarui!")
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.info("""
        ### 💡 Panduan Parameter Investasi
        
        **📉 Inflasi Indonesia (Historis):**
        - Rata-rata jangka panjang: 3-6% per tahun
        - Target Bank Indonesia: 2-4% per tahun
        
        **📈 Return Investasi (Historis):**
        - **Saham (IHSG)**: 8-15% per tahun (risiko tinggi)
        - **Reksadana Campuran**: 7-12% per tahun (risiko menengah)
        - **Obligasi**: 6-10% per tahun (risiko rendah)
        - **Deposito**: 4-7% per tahun (risiko sangat rendah)
        
        *Gunakan asumsi konservatif untuk proyeksi yang lebih aman*
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='
    text-align: center; 
    padding: 1.5rem; 
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
    border-radius: 16px; 
    margin-top: 2rem; 
    border: 2px solid #475569;
'>
    <p style='
        color: #cbd5f5; 
        font-weight: 600; 
        margin-bottom: 0.5rem;
    '>
        © 2026 @akbaralqahri
    </p>
    <p style='
        color: #94a3b8; 
        font-size: 0.875rem;
    '>
        <a href='https://www.linkedin.com/in/akbaralqahri/' target='_blank' 
           style='color: #a78bfa; text-decoration: none; font-weight: 500;'>
            LinkedIn
        </a>
        &nbsp;•&nbsp;
        <a href='https://akbaralqahri.github.io/portofolio/' target='_blank' 
           style='color: #ec4899; text-decoration: none; font-weight: 500;'>
            Portfolio
        </a>
    </p>
</div>
""", unsafe_allow_html=True)
