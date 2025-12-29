"""
🚀 DEEP SPACE FUSION - AI OPERATIONS DASHBOARD
World-Class MLOps Control Center - Streamlit Edition

A groundbreaking, futuristic AI Operations Dashboard featuring comprehensive
MLOps management capabilities with stunning visual design.
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Operations Dashboard | MLOps Control Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS - DEEP SPACE FUSION THEME
# ==========================================

def load_custom_css():
    st.markdown("""
    <style>
    /* Import Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root Variables */
    :root {
        --obsidian-black: #0a0a0f;
        --midnight-navy: #1a1a2e;
        --deep-space: #16213e;
        --electric-violet: #8B5CF6;
        --neon-cyan: #00F0FF;
        --zen-purple: #A855F7;
        --success-green: #10B981;
        --warning-orange: #F59E0B;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #16213e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dynamic Title Gradient */
    .dynamic-title {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #8B5CF6, #00F0FF, #A855F7, #8B5CF6);
        background-size: 300% 100%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 8s linear infinite;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .section-subtitle {
        text-align: center;
        color: #888;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 2rem;
    }
    
    /* Glass Cards */
    .glass-card {
        background: rgba(26, 26, 46, 0.6);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .glass-card:hover {
        border-color: rgba(139, 92, 246, 0.5);
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(139, 92, 246, 0.3);
    }
    
    /* KPI Cards */
    .kpi-card {
        background: rgba(26, 26, 46, 0.6);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 150px;
        height: 150px;
        background: radial-gradient(circle, var(--electric-violet), transparent);
        opacity: 0.2;
        filter: blur(40px);
        pointer-events: none;
    }
    
    .kpi-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .kpi-label {
        font-size: 0.75rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .kpi-value {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #8B5CF6, #00F0FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .kpi-trend {
        font-size: 0.8rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.25rem;
    }
    
    .trend-positive { color: #10B981; }
    .trend-negative { color: #EF4444; }
    .trend-neutral { color: #888; }
    
    /* Status Badge */
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin: 0.25rem;
    }
    
    .status-success {
        background: rgba(16, 185, 129, 0.2);
        color: #10B981;
    }
    
    .status-running {
        background: rgba(0, 240, 255, 0.2);
        color: #00F0FF;
    }
    
    .status-warning {
        background: rgba(245, 158, 11, 0.2);
        color: #F59E0B;
    }
    
    .status-pending {
        background: rgba(168, 85, 247, 0.2);
        color: #A855F7;
    }
    
    /* Metric Cards */
    .metric-card {
        background: rgba(26, 26, 46, 0.6);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        filter: drop-shadow(0 0 10px #8B5CF6);
    }
    
    .metric-label {
        font-size: 0.75rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-family: 'Orbitron', monospace;
        font-size: 2rem;
        font-weight: 900;
        background: linear-gradient(135deg, #8B5CF6, #00F0FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Timeline */
    .timeline-item {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        position: relative;
    }
    
    .timeline-marker {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        border: 3px solid #1a1a2e;
        flex-shrink: 0;
    }
    
    .marker-success {
        background: #10B981;
        box-shadow: 0 0 15px #10B981;
    }
    
    .marker-warning {
        background: #F59E0B;
        box-shadow: 0 0 15px #F59E0B;
    }
    
    .timeline-content {
        flex: 1;
    }
    
    .timeline-time {
        font-size: 0.7rem;
        color: #666;
        margin-bottom: 0.25rem;
    }
    
    .timeline-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #e0e0e0;
        margin-bottom: 0.25rem;
    }
    
    .timeline-desc {
        font-size: 0.8rem;
        color: #888;
    }
    
    /* Custom Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(26, 26, 46, 0.6);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 0.75rem;
        border: 1px solid rgba(139, 92, 246, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: #888;
        font-weight: 500;
        padding: 0.75rem 1.5rem;
        border: 1px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(139, 92, 246, 0.1);
        border-color: rgba(139, 92, 246, 0.3);
        color: #e0e0e0;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(0, 240, 255, 0.1));
        border-color: #8B5CF6;
        color: #00F0FF;
    }
    
    /* Container Cards */
    .container-card {
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 0.75rem;
    }
    
    .container-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.5rem;
    }
    
    .container-icon {
        font-size: 1.25rem;
    }
    
    .container-name {
        flex: 1;
        font-weight: 600;
        color: #e0e0e0;
    }
    
    /* Data Table Styling */
    .dataframe {
        background: rgba(26, 26, 46, 0.6) !important;
        border-radius: 12px;
        border: 1px solid rgba(139, 92, 246, 0.2) !important;
    }
    
    .dataframe th {
        background: rgba(139, 92, 246, 0.1) !important;
        color: #00F0FF !important;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.7rem;
        letter-spacing: 0.5px;
    }
    
    .dataframe td {
        color: #e0e0e0 !important;
        border-color: rgba(139, 92, 246, 0.1) !important;
    }
    
    /* Plotly Charts */
    .js-plotly-plot {
        border-radius: 15px;
        overflow: hidden;
    }
    
    /* Success/Info/Warning boxes */
    .stAlert {
        background: rgba(26, 26, 46, 0.6);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 12px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a2e;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #8B5CF6, #A855F7);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #A855F7, #00F0FF);
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# DATA GENERATION FUNCTIONS
# ==========================================

@st.cache_data
def generate_performance_data():
    """Generate performance telemetry data"""
    dates = pd.date_range(end=datetime.now(), periods=30, freq='H')
    data = pd.DataFrame({
        'timestamp': dates,
        'accuracy': 70 + np.sin(np.arange(30) * 0.3) * 20 + np.random.randn(30) * 3,
        'latency': 25 + np.random.randn(30) * 5,
        'throughput': 1000 + np.random.randn(30) * 100
    })
    return data

@st.cache_data
def generate_drift_data():
    """Generate data drift distribution"""
    bins = 50
    x = np.linspace(-5, 5, bins)
    baseline = 100 * np.exp(-0.5 * x**2)
    current = 90 * np.exp(-0.5 * (x - 0.5)**2) + np.random.randn(bins) * 5
    
    df = pd.DataFrame({
        'x': x,
        'baseline': baseline,
        'current': current
    })
    return df

@st.cache_data
def generate_resource_data():
    """Generate resource metrics time series"""
    timestamps = pd.date_range(end=datetime.now(), periods=20, freq='min')
    data = pd.DataFrame({
        'timestamp': timestamps,
        'cpu': np.random.rand(20) * 100,
        'memory': 40 + np.random.rand(20) * 30,
        'gpu': 60 + np.random.rand(20) * 40,
        'network': np.random.rand(20) * 300
    })
    return data

@st.cache_data
def generate_pipeline_history():
    """Generate pipeline execution history"""
    data = pd.DataFrame({
        'Pipeline ID': ['pipe-7f8a9', 'pipe-6e7b8', 'pipe-5d6c7', 'pipe-4c5b6', 'pipe-3b4a5'],
        'Started': [
            '2024-12-29 18:45 UTC',
            '2024-12-29 14:20 UTC',
            '2024-12-29 10:15 UTC',
            '2024-12-29 06:30 UTC',
            '2024-12-28 22:00 UTC'
        ],
        'Duration': ['45m 23s', '1h 12m', '58m 47s', '1h 5m', '52m 19s'],
        'Status': ['Running', 'Success', 'Success', 'Success', 'Success'],
        'Triggered By': ['Schedule', 'Manual', 'CI/CD', 'Schedule', 'Manual']
    })
    return data

@st.cache_data
def generate_cost_data():
    """Generate cost analysis data"""
    data = pd.DataFrame({
        'Category': ['Compute', 'Storage', 'Network', 'Other'],
        'Percentage': [45, 25, 15, 15],
        'Color': ['#8B5CF6', '#00F0FF', '#A855F7', '#6366F1']
    })
    return data

# ==========================================
# CHART CREATION FUNCTIONS
# ==========================================

def create_performance_chart(data, color_scheme='violet'):
    """Create performance telemetry chart"""
    colors = {
        'violet': '#8B5CF6',
        'cyan': '#00F0FF',
        'purple': '#A855F7',
        'green': '#10B981'
    }
    color = colors.get(color_scheme, '#8B5CF6')
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['timestamp'],
        y=data['accuracy'],
        mode='lines+markers',
        name='Model Accuracy',
        line=dict(color=color, width=3, shape='spline'),
        marker=dict(size=6, color='#00F0FF', line=dict(color=color, width=2)),
        fill='tozeroy',
        fillcolor=f'rgba(139, 92, 246, 0.2)',
        hovertemplate='<b>Accuracy</b>: %{y:.2f}%<br><b>Time</b>: %{x}<extra></extra>'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0', family='Inter'),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(139, 92, 246, 0.1)',
            zeroline=False,
            color='#888'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(139, 92, 246, 0.1)',
            zeroline=False,
            color='#888',
            title='Accuracy (%)'
        ),
        hovermode='x unified',
        height=400,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    
    return fig

def create_drift_chart(data):
    """Create drift distribution comparison chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['x'],
        y=data['baseline'],
        name='Baseline',
        marker=dict(color='rgba(139, 92, 246, 0.5)'),
        hovertemplate='<b>Baseline</b>: %{y:.1f}<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        x=data['x'],
        y=data['current'],
        name='Current',
        marker=dict(color='rgba(0, 240, 255, 0.5)'),
        hovertemplate='<b>Current</b>: %{y:.1f}<extra></extra>'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0', family='Inter'),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            color='#888',
            title='Feature Value'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(139, 92, 246, 0.1)',
            zeroline=False,
            color='#888',
            title='Frequency'
        ),
        barmode='overlay',
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def create_cost_chart(data):
    """Create cost analysis donut chart"""
    fig = go.Figure(data=[go.Pie(
        labels=data['Category'],
        values=data['Percentage'],
        hole=0.6,
        marker=dict(
            colors=data['Color'],
            line=dict(color='#1a1a2e', width=2)
        ),
        textinfo='label+percent',
        textfont=dict(size=12, color='#e0e0e0'),
        hovertemplate='<b>%{label}</b><br>%{value}%<extra></extra>'
    )])
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0', family='Inter'),
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.1
        )
    )
    
    return fig

def create_resource_sparkline(data, metric, color='#00F0FF'):
    """Create mini sparkline chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['timestamp'],
        y=data[metric],
        mode='lines',
        line=dict(color=color, width=2),
        fill='tozeroy',
        fillcolor=f'rgba(0, 240, 255, 0.2)',
        hovertemplate='%{y:.1f}<extra></extra>'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=80,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False
    )
    
    return fig

def create_3d_topology():
    """Create 3D cluster topology visualization"""
    # Generate random 3D node positions
    np.random.seed(42)
    n_nodes = 20
    
    x = np.random.rand(n_nodes) * 10
    y = np.random.rand(n_nodes) * 10
    z = np.random.rand(n_nodes) * 10
    
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=10,
            color=z,
            colorscale=[[0, '#8B5CF6'], [0.5, '#00F0FF'], [1, '#A855F7']],
            showscale=False,
            line=dict(color='#00F0FF', width=2)
        ),
        text=[f'Node {i+1}' for i in range(n_nodes)],
        hovertemplate='<b>%{text}</b><br>X: %{x:.2f}<br>Y: %{y:.2f}<br>Z: %{z:.2f}<extra></extra>'
    )])
    
    # Add connections
    for i in range(n_nodes - 1):
        fig.add_trace(go.Scatter3d(
            x=[x[i], x[i+1]],
            y=[y[i], y[i+1]],
            z=[z[i], z[i+1]],
            mode='lines',
            line=dict(color='rgba(0, 240, 255, 0.2)', width=2),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='rgba(0,0,0,0)'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False
    )
    
    return fig

def create_lineage_graph():
    """Create model lineage flow diagram"""
    fig = go.Figure()
    
    # Define stages with adjusted positions to prevent overlap
    stages = ['Data\nIngestion', 'Feature\nEngineering', 'Model\nTraining', 'Validation', 'Deployment']
    x_pos = [1, 2, 3, 4, 5]
    y_pos = [2.2, 2.2, 2.2, 2.2, 2.2]  # Slightly higher to prevent overlap
    
    # IMPORTANT: Add connections FIRST (so they appear behind nodes)
    for i in range(len(x_pos) - 1):
        fig.add_trace(go.Scatter(
            x=[x_pos[i], x_pos[i+1]],
            y=[y_pos[i], y_pos[i+1]],
            mode='lines',
            line=dict(color='rgba(139, 92, 246, 0.3)', width=3),  # Semi-transparent line
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Add version branch line (before nodes)
    fig.add_trace(go.Scatter(
        x=[3, 3],
        y=[2.2, 1.3],  # Adjusted vertical position
        mode='lines',
        line=dict(color='rgba(168, 85, 247, 0.4)', width=2, dash='dash'),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add nodes with text ON TOP (after lines)
    for i, (stage, x, y) in enumerate(zip(stages, x_pos, y_pos)):
        color = '#8B5CF6' if i % 2 == 0 else '#00F0FF'
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers+text',
            marker=dict(size=60, color=color, line=dict(color='#e0e0e0', width=2)),
            text=stage,
            textposition='middle center',
            textfont=dict(size=11, color='#0a0a0f', weight=700),  # Dark text for better contrast
            showlegend=False,
            hovertemplate=f'<b>{stage}</b><extra></extra>'
        ))
    
    # Add version branch marker (on top)
    fig.add_trace(go.Scatter(
        x=[3],
        y=[1.3],
        mode='markers+text',
        marker=dict(size=40, color='#1a1a2e', line=dict(color='#A855F7', width=2)),
        text='v2.0',
        textposition='middle center',
        textfont=dict(size=10, color='#A855F7', weight=600),
        showlegend=False,
        hovertemplate='<b>Version 2.0</b><br>June 2024<extra></extra>'
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(visible=False, range=[0.5, 5.5]),
        yaxis=dict(visible=False, range=[0.8, 2.8]),  # Adjusted range to accommodate higher nodes
        height=450,  # Increased height for better spacing
        margin=dict(l=30, r=30, t=40, b=40),  # Increased margins
        hovermode='closest'
    )
    
    return fig

# ==========================================
# MAIN APPLICATION
# ==========================================

def main():
    # Auto-refresh every 30 seconds (30000 milliseconds)
    st_autorefresh(interval=30000, key="datarefresh")
    
    # Load custom CSS
    load_custom_css()
    
    # Header with dynamic title
    st.markdown('<h1 class="dynamic-title">AI OPERATIONS CONTROL CENTER</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Deep Space Fusion MLOps Dashboard</p>', unsafe_allow_html=True)
    
    # Status bar
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        st.markdown(f"""
        <div style="text-align: center;">
            <span class="status-badge status-success">● SYSTEM ONLINE</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="text-align: center; color: #00F0FF; font-family: Orbitron;">
            {datetime.now().strftime('%H:%M:%S')}
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="text-align: center; color: #888; font-size: 0.8rem;">
            12 Active Models
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div style="text-align: center; color: #888; font-size: 0.8rem;">
            v2.5.1
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview",
        "🔗 Model Lineage",
        "📉 Data Drift",
        "⚙️ Pipeline Orchestration",
        "💻 Resource Metrics"
    ])
    
    # ==========================================
    # TAB 1: OVERVIEW
    # ==========================================
    
    with tab1:
        st.markdown('<h2 class="dynamic-title" style="font-size: 1.8rem;">Mission Control Overview</h2>', unsafe_allow_html=True)
        st.markdown('<p class="section-subtitle">Real-time MLOps Intelligence Dashboard</p>', unsafe_allow_html=True)
        
        # KPI Cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="kpi-card">
                <div class="kpi-icon">🎯</div>
                <div class="kpi-label">Model Accuracy</div>
                <div class="kpi-value">94.7<span style="font-size: 1rem; color: #888;">%</span></div>
                <div class="kpi-trend trend-positive">
                    <span>↑</span> 2.3% from last week
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="kpi-card">
                <div class="kpi-icon">⚡</div>
                <div class="kpi-label">Inference Speed</div>
                <div class="kpi-value">28<span style="font-size: 1rem; color: #888;">ms</span></div>
                <div class="kpi-trend trend-positive">
                    <span>↓</span> 15% faster
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="kpi-card">
                <div class="kpi-icon">📦</div>
                <div class="kpi-label">Active Models</div>
                <div class="kpi-value">12<span style="font-size: 1rem; color: #888;"></span></div>
                <div class="kpi-trend trend-neutral">
                    <span>→</span> Stable deployment
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Charts Row
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 📈 Performance Telemetry")
            
            # Color scheme selector
            color_scheme = st.selectbox(
                "Color Scheme",
                ["violet", "cyan", "purple", "green"],
                key="perf_color",
                label_visibility="collapsed"
            )
            
            perf_data = generate_performance_data()
            fig = create_performance_chart(perf_data, color_scheme)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 💚 System Health Matrix")
            
            health_data = {
                'Component': ['API Gateway', 'Model Registry', 'Data Pipeline', 'Training Cluster', 'Monitoring Stack'],
                'Health': [98, 95, 89, 92, 100]
            }
            
            for component, health in zip(health_data['Component'], health_data['Health']):
                status = 'excellent' if health >= 95 else 'good' if health >= 85 else 'warning'
                color = '#10B981' if health >= 95 else '#8B5CF6' if health >= 85 else '#F59E0B'
                
                st.markdown(f"""
                <div style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                        <span style="color: #e0e0e0; font-size: 0.85rem;">{component}</span>
                        <span style="color: {color}; font-family: Orbitron; font-size: 0.85rem;">{health}%</span>
                    </div>
                    <div style="width: 100%; height: 8px; background: rgba(139, 92, 246, 0.1); border-radius: 4px; overflow: hidden;">
                        <div style="width: {health}%; height: 100%; background: linear-gradient(90deg, {color}, #00F0FF); border-radius: 4px; box-shadow: 0 0 10px {color};"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Project Architecture
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📁 Project Architecture Analysis")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **📄 Configuration Files**
            - `dvc.yaml` - Pipeline Config
            - `params.yaml` - Parameters
            - `prometheus.yml` - Monitoring
            """)
        
        with col2:
            st.markdown("""
            **🐳 Container Setup**
            - `docker-compose.yml`
            - `Dockerfile`
            - 3 Active Containers
            """)
        
        with col3:
            st.markdown("""
            **📊 Data & Models**
            - `/data` - Datasets
            - `/models` - Trained Models
            - `/reports` - Analytics
            """)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================
    # TAB 2: MODEL LINEAGE
    # ==========================================
    
    with tab2:
        st.markdown('<h2 class="dynamic-title" style="font-size: 1.8rem;">Model Lineage & Provenance</h2>', unsafe_allow_html=True)
        st.markdown('<p class="section-subtitle">End-to-end model genealogy visualization</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🔗 Interactive Lineage Graph")
        
        # Add spacing before graph to prevent overlap
        st.markdown('<div style="margin-top: 1.5rem; margin-bottom: 2rem;">', unsafe_allow_html=True)
        fig = create_lineage_graph()
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Add spacing before metadata section
        st.markdown('<div style="margin-top: 2rem;">', unsafe_allow_html=True)
        st.markdown("#### 📋 Model Metadata")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            **Created By:**  
            MLOps Pipeline
            """)
        with col2:
            st.markdown("""
            **Framework:**  
            TensorFlow 2.14
            """)
        with col3:
            st.markdown("""
            **Dataset Version:**  
            v3.2.1
            """)
        with col4:
            st.markdown("""
            **Training Duration:**  
            2h 34m
            """)
        
        # Close the metadata spacing div
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Model Versions
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("#### 🏷️ Current Version")
            st.markdown("""
            <div style="text-align: center;">
                <div class="metric-value">v2.0</div>
                <p style="color: #888; font-size: 0.9rem;">Deployed: June 2024</p>
                <span class="status-badge status-success">Production</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("#### 🕐 Previous Version")
            st.markdown("""
            <div style="text-align: center;">
                <div class="metric-value">v1.0</div>
                <p style="color: #888; font-size: 0.9rem;">Archived: March 2024</p>
                <span class="status-badge status-warning">Deprecated</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================
    # TAB 3: DATA DRIFT
    # ==========================================
    
    with tab3:
        st.markdown('<h2 class="dynamic-title" style="font-size: 1.8rem;">Data Drift Detection</h2>', unsafe_allow_html=True)
        st.markdown('<p class="section-subtitle">Real-time distribution shift analysis</p>', unsafe_allow_html=True)
        
        # Drift Metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-icon">📊</div>
                <div class="metric-label">Population Stability</div>
                <div class="metric-value">0.089</div>
                <span class="status-badge status-success">Stable</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-icon">⚠️</div>
                <div class="metric-label">Feature Drift Score</div>
                <div class="metric-value">0.234</div>
                <span class="status-badge status-warning">Monitor</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-icon">✓</div>
                <div class="metric-label">Concept Drift</div>
                <div class="metric-value">0.012</div>
                <span class="status-badge status-success">No Drift</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Distribution Chart
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📊 Feature Distribution Analysis")
        
        drift_data = generate_drift_data()
        fig = create_drift_chart(drift_data)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Drift Timeline
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### ⏱️ Drift Alert Timeline")
        
        st.markdown("""
        <div class="timeline-item">
            <div class="timeline-marker marker-success"></div>
            <div class="timeline-content">
                <div class="timeline-time">2 hours ago</div>
                <div class="timeline-title">Drift Check Passed</div>
                <div class="timeline-desc">All features within acceptable range</div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-marker marker-warning"></div>
            <div class="timeline-content">
                <div class="timeline-time">6 hours ago</div>
                <div class="timeline-title">Minor Drift Detected</div>
                <div class="timeline-desc">Feature 'store_location' showing mild variance</div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-marker marker-success"></div>
            <div class="timeline-content">
                <div class="timeline-time">12 hours ago</div>
                <div class="timeline-title">Drift Check Passed</div>
                <div class="timeline-desc">Distributions aligned with baseline</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================
    # TAB 4: PIPELINE ORCHESTRATION
    # ==========================================
    
    with tab4:
        st.markdown('<h2 class="dynamic-title" style="font-size: 1.8rem;">Pipeline Orchestration</h2>', unsafe_allow_html=True)
        st.markdown('<p class="section-subtitle">DVC/MLflow workflow visualization</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 🔄 Active Pipelines")
            
            st.markdown("""
            <div class="container-card">
                <div class="container-header">
                    <span class="container-icon">🔄</span>
                    <span class="container-name">Retail Demand Training</span>
                    <span class="status-badge status-running">Running</span>
                </div>
                <div style="color: #666; font-size: 0.75rem; margin-bottom: 0.5rem;">Started 45m ago</div>
                <div style="margin-bottom: 0.5rem;">
                    <div style="width: 100%; height: 6px; background: rgba(139, 92, 246, 0.2); border-radius: 3px; overflow: hidden;">
                        <div style="width: 67%; height: 100%; background: linear-gradient(90deg, #8B5CF6, #00F0FF); border-radius: 3px; box-shadow: 0 0 10px #00F0FF;"></div>
                    </div>
                </div>
                <div style="color: #888; font-size: 0.7rem;">Step 4/6: Model Training</div>
            </div>
            
            <div class="container-card">
                <div class="container-header">
                    <span class="container-icon">✓</span>
                    <span class="container-name">Data Validation</span>
                    <span class="status-badge status-success">Success</span>
                </div>
                <div style="color: #666; font-size: 0.75rem;">Completed 2h ago</div>
            </div>
            
            <div class="container-card">
                <div class="container-header">
                    <span class="container-icon">⏸</span>
                    <span class="container-name">Model Deployment</span>
                    <span class="status-badge status-pending">Pending</span>
                </div>
                <div style="color: #666; font-size: 0.75rem;">Scheduled in 1h</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 🔀 Pipeline DAG")
            
            st.markdown("""
            <div style="text-align: center; padding: 2rem;">
                <div style="display: inline-block; margin: 0.5rem;">
                    <div style="width: 80px; padding: 1rem; background: rgba(139, 92, 246, 0.2); border: 2px solid #8B5CF6; border-radius: 10px; color: #8B5CF6; font-weight: 600;">
                        Data Prep
                    </div>
                </div>
                <div style="color: #8B5CF6; margin: 0.25rem;">↓</div>
                <div style="display: inline-block; margin: 0.5rem;">
                    <div style="width: 80px; padding: 1rem; background: rgba(139, 92, 246, 0.2); border: 2px solid #8B5CF6; border-radius: 10px; color: #8B5CF6; font-weight: 600;">
                        Features
                    </div>
                </div>
                <div style="color: #8B5CF6; margin: 0.25rem;">↓</div>
                <div style="display: inline-block; margin: 0.5rem;">
                    <div style="width: 80px; padding: 1rem; background: rgba(0, 240, 255, 0.2); border: 2px solid #00F0FF; border-radius: 10px; color: #00F0FF; font-weight: 600;">
                        Training
                    </div>
                </div>
                <div style="color: #8B5CF6; margin: 0.25rem;">↓</div>
                <div style="display: inline-block; margin: 0.5rem;">
                    <div style="width: 80px; padding: 1rem; background: rgba(139, 92, 246, 0.2); border: 2px solid #8B5CF6; border-radius: 10px; color: #8B5CF6; font-weight: 600;">
                        Evaluation
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Execution History
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📜 Execution History")
        
        history_data = generate_pipeline_history()
        st.dataframe(history_data, use_container_width=True, hide_index=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================
    # TAB 5: RESOURCE METRICS
    # ==========================================
    
    with tab5:
        st.markdown('<h2 class="dynamic-title" style="font-size: 1.8rem;">Resource Metrics & Telemetry</h2>', unsafe_allow_html=True)
        st.markdown('<p class="section-subtitle">Infrastructure performance monitoring</p>', unsafe_allow_html=True)
        
        # Resource Cards with Sparklines
        resource_data = generate_resource_data()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("🖥️")
            st.markdown('<div class="metric-label">CPU Usage</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">67<span style="font-size: 1rem; color: #888;">%</span></div>', unsafe_allow_html=True)
            fig = create_resource_sparkline(resource_data, 'cpu')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("💾")
            st.markdown('<div class="metric-label">Memory</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">45.2<span style="font-size: 0.8rem; color: #888;">GB</span></div>', unsafe_allow_html=True)
            fig = create_resource_sparkline(resource_data, 'memory')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("🎮")
            st.markdown('<div class="metric-label">GPU Compute</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">82<span style="font-size: 1rem; color: #888;">%</span></div>', unsafe_allow_html=True)
            fig = create_resource_sparkline(resource_data, 'gpu')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("🌐")
            st.markdown('<div class="metric-label">Network I/O</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">234<span style="font-size: 0.8rem; color: #888;">Mbps</span></div>', unsafe_allow_html=True)
            fig = create_resource_sparkline(resource_data, 'network')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 3D Topology
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🌌 3D Cluster Topology")
        
        fig_3d = create_3d_topology()
        st.plotly_chart(fig_3d, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Container Resources and Cost Analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 🐳 Container Resources")
            
            st.markdown("""
            <div class="container-card">
                <div class="container-header">
                    <span class="container-icon">🐳</span>
                    <span class="container-name">mlflow-server</span>
                    <span class="status-badge status-success">Active</span>
                </div>
                <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
                    <div style="font-size: 0.75rem;"><span style="color: #666;">CPU:</span> <span style="color: #00F0FF; font-weight: 600;">23%</span></div>
                    <div style="font-size: 0.75rem;"><span style="color: #666;">MEM:</span> <span style="color: #00F0FF; font-weight: 600;">2.1 GB</span></div>
                </div>
            </div>
            
            <div class="container-card">
                <div class="container-header">
                    <span class="container-icon">🐳</span>
                    <span class="container-name">prometheus</span>
                    <span class="status-badge status-success">Active</span>
                </div>
                <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
                    <div style="font-size: 0.75rem;"><span style="color: #666;">CPU:</span> <span style="color: #00F0FF; font-weight: 600;">12%</span></div>
                    <div style="font-size: 0.75rem;"><span style="color: #666;">MEM:</span> <span style="color: #00F0FF; font-weight: 600;">1.8 GB</span></div>
                </div>
            </div>
            
            <div class="container-card">
                <div class="container-header">
                    <span class="container-icon">🐳</span>
                    <span class="container-name">grafana</span>
                    <span class="status-badge status-success">Active</span>
                </div>
                <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
                    <div style="font-size: 0.75rem;"><span style="color: #666;">CPU:</span> <span style="color: #00F0FF; font-weight: 600;">8%</span></div>
                    <div style="font-size: 0.75rem;"><span style="color: #666;">MEM:</span> <span style="color: #00F0FF; font-weight: 600;">892 MB</span></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 💰 Cost Analysis")
            
            cost_data = generate_cost_data()
            fig_cost = create_cost_chart(cost_data)
            st.plotly_chart(fig_cost, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.75rem; padding: 2rem 0;">
        🚀 Deep Space Fusion MLOps Dashboard | Built with ❤️ by Shehab Hegab | v1.0.0
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
