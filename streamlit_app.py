import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="JE & Chikungunya Teaching Dashboard",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(45deg, #3498db, #2980b9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #34495e;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .stat-card {
        background: linear-gradient(45deg, #27ae60, #2ecc71);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }
    .stat-card:hover {
        transform: translateY(-5px);
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    .sidebar-header {
        font-size: 1.3rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown('<div class="sidebar-header">🦟 JE & Chikungunya Dashboard</div>', unsafe_allow_html=True)
st.sidebar.markdown("---")

# Navigation menu
page = st.sidebar.selectbox(
    "Navigate to Section",
    ["🏠 Overview", "📊 Epidemiology", "🔬 Clinical Features", "🛡️ Prevention", "📈 Visualizations", "📝 Assessment", "🎬 Video Content", "📚 Resources"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**CBME Aligned Content**")
st.sidebar.markdown("National Medical Commission")
st.sidebar.markdown("Community Medicine Curriculum")
st.sidebar.markdown("MBBS Teaching Material")

# Main content based on navigation
if page == "🏠 Overview":
    st.markdown('<h1 class="main-header">Japanese Encephalitis & Chikungunya</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #7f8c8d;">Comprehensive Teaching Dashboard for MBBS Students</h2>', unsafe_allow_html=True)

    # Key statistics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">100,000+</div>
            <div class="stat-label">Annual JE Cases Globally</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">1.3M</div>
            <div class="stat-label">2006 Chikungunya Outbreak India</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">24</div>
            <div class="stat-label">JE Endemic Countries</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">110+</div>
            <div class="stat-label">Countries with Chikungunya</div>
        </div>
        """, unsafe_allow_html=True)

    # Introduction
    st.markdown('<h2 class="section-header">About This Dashboard</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>🎯 Learning Objectives</h3>
            <ul>
                <li>Understand global and Indian epidemiology of JE and Chikungunya</li>
                <li>Learn clinical features, diagnosis, and treatment approaches</li>
                <li>Master prevention and control strategies under NVBDCP</li>
                <li>Compare both diseases and their public health impact</li>
                <li>Apply knowledge in community medicine practice</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box">
            <h3>📋 CBME Alignment</h3>
            <p>This material addresses core competencies in:</p>
            <ul>
                <li><strong>Community Medicine:</strong> Epidemiology and disease control</li>
                <li><strong>Preventive Medicine:</strong> Vector control and health promotion</li>
                <li><strong>Clinical Practice:</strong> Diagnosis and management of VBDs</li>
                <li><strong>Public Health:</strong> Surveillance and outbreak response</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Quick facts
    st.markdown('<h2 class="section-header">Quick Facts</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🦟 Disease Overview", "📊 Indian Burden", "🎯 Prevention Focus"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Japanese Encephalitis (JE)")
            st.write("**Vector:** Culex tritaeniorhynchus")
            st.write("**Transmission:** Enzootic cycle (mosquito-pig/bird-human)")
            st.write("**Clinical:** Encephalitis, neurological deficits")
            st.write("**Fatality:** 20-30% in severe cases")
            st.write("**Indian Program:** Universal Immunization Programme (UIP)")

        with col2:
            st.subheader("Chikungunya")
            st.write("**Vector:** Aedes aegypti/albopictus")
            st.write("**Transmission:** Human-mosquito-human cycle")
            st.write("**Clinical:** Severe joint pain, chronic arthritis")
            st.write("**Fatality:** <0.1% (rarely fatal)")
            st.write("**Indian Program:** NVBDCP source reduction")

    with tab2:
        st.subheader("Indian Disease Burden")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**JE High Burden States:**")
            st.write("- Uttar Pradesh: 40% of cases")
            st.write("- Bihar: 25% of cases")
            st.write("- Assam: 15% of cases")
            st.write("- West Bengal: 10% of cases")

        with col2:
            st.write("**Chikungunya Outbreak Areas:**")
            st.write("- Delhi: Major urban outbreaks")
            st.write("- Kerala: 2006 epidemic epicenter")
            st.write("- Karnataka: Recurrent outbreaks")
            st.write("- Maharashtra: Urban transmission")

    with tab3:
        st.subheader("Prevention Strategies")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**JE Prevention (95% effective):**")
            st.write("✅ Vaccination (UIP)")
            st.write("✅ Vector control (NVBDCP)")
            st.write("✅ Personal protection")
            st.write("✅ Surveillance (IDSP)")

        with col2:
            st.write("**Chikungunya Prevention (95% effective):**")
            st.write("✅ Source reduction")
            st.write("✅ Vector control (NVBDCP)")
            st.write("✅ Community education")
            st.write("✅ Personal protection")

elif page == "📊 Epidemiology":
    st.markdown('<h1 class="main-header">Epidemiology Dashboard</h1>', unsafe_allow_html=True)

    # Global vs Indian epidemiology
    st.markdown('<h2 class="section-header">Global vs Indian Epidemiology</h2>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🌍 Global Perspective", "🇮🇳 Indian Context"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Japanese Encephalitis - Global")
            st.write("**Endemic Regions:**")
            st.write("• South-East Asia: India, Bangladesh, Myanmar, Thailand")
            st.write("• Western Pacific: China, Japan, Philippines")
            st.write("• Annual cases: ~100,000 (95% CI: 61,720–157,522)")
            st.write("• At risk: >3 billion people")
            st.write("• Case fatality: 20-30%")

            # Display global JE map visualization
            if os.path.exists('je_cases_india.png'):
                st.image('je_cases_india.png', caption='Global JE Distribution', use_column_width=True)

        with col2:
            st.subheader("Chikungunya - Global")
            st.write("**Distribution:**")
            st.write("• 110+ countries affected since 1952")
            st.write("• Africa: Tanzania, Kenya (endemic)")
            st.write("• Asia: India, Thailand, Indonesia")
            st.write("• Americas: Brazil, Mexico (recent)")
            st.write("• Case fatality: <0.1%")

            # Display global chikungunya visualization
            if os.path.exists('chikungunya_cases_india.png'):
                st.image('chikungunya_cases_india.png', caption='Global Chikungunya Distribution', use_column_width=True)

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("JE in India")
            st.write("**High Burden States:**")
            st.write("• Uttar Pradesh: 5,000 cases")
            st.write("• Bihar: 3,000 cases")
            st.write("• Assam: 2,000 cases")
            st.write("• West Bengal: 1,500 cases")
            st.write("**Seasonal Pattern:** July-October (monsoon)")
            st.write("**Risk Factors:** Rice farming, pig rearing")

        with col2:
            st.subheader("Chikungunya in India")
            st.write("**Major Outbreaks:**")
            st.write("• Delhi: 8,000 cases")
            st.write("• Kerala: 6,000 cases")
            st.write("• Karnataka: 4,000 cases")
            st.write("• Maharashtra: 3,000 cases")
            st.write("**Pattern:** Urban and rural transmission")
            st.write("**Vectors:** Aedes aegypti (urban), Aedes albopictus (rural)")

        # State-wise comparison
        st.markdown('<h3 style="color: #e74c3c;">State-wise Burden Comparison</h3>', unsafe_allow_html=True)
        if os.path.exists('india_state_burden.png'):
            st.image('india_state_burden.png', caption='State-wise Disease Burden in India', use_column_width=True)

elif page == "🔬 Clinical Features":
    st.markdown('<h1 class="main-header">Clinical Features & Diagnosis</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Symptom Timeline Comparison</h2>', unsafe_allow_html=True)

    if os.path.exists('symptom_timeline.png'):
        st.image('symptom_timeline.png', caption='Clinical Symptom Timeline Comparison', use_column_width=True)

    # Clinical comparison table
    st.markdown('<h2 class="section-header">Clinical Comparison</h2>', unsafe_allow_html=True)

    clinical_data = {
        'Feature': ['Incubation Period', 'Primary Symptom', 'Fatality Rate', 'Chronic Issues', 'Age Group Most Affected', 'Indian Presentation'],
        'JE': ['4-14 days', 'Encephalitis (CNS)', '20-30%', 'Neurological deficits (30-50%)', 'Children <15 years', 'Acute Encephalitis Syndrome (AES)'],
        'Chikungunya': ['4-8 days', 'Severe joint pain', '<0.1%', 'Chronic arthritis (10-30%)', 'All ages (adults more symptomatic)', '"Chikungunya gait"']
    }

    df_clinical = pd.DataFrame(clinical_data)
    st.table(df_clinical)

    # Transmission cycles
    st.markdown('<h2 class="section-header">Transmission Cycles</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("JE Transmission Cycle")
        if os.path.exists('je_transmission_cycle.png'):
            st.image('je_transmission_cycle.png', caption='JE Enzootic Cycle in Rural India', use_column_width=True)
        st.write("**Cycle:** Mosquito → Pig/Bird → Human")
        st.write("**Indian Context:** Rice fields, pig farms, monsoon season")

    with col2:
        st.subheader("Chikungunya Transmission Cycle")
        if os.path.exists('chikungunya_transmission_cycle.png'):
            st.image('chikungunya_transmission_cycle.png', caption='Chikungunya Human-Mosquito Cycle', use_column_width=True)
        st.write("**Cycle:** Human → Mosquito → Human")
        st.write("**Indian Context:** Water storage, poor sanitation, urban areas")

elif page == "🛡️ Prevention":
    st.markdown('<h1 class="main-header">Prevention & Control Strategies</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Prevention Measures Effectiveness</h2>', unsafe_allow_html=True)

    if os.path.exists('prevention_measures.png'):
        st.image('prevention_measures.png', caption='Prevention Measures Effectiveness Comparison', use_column_width=True)

    # Prevention strategies comparison
    st.markdown('<h2 class="section-header">Detailed Prevention Strategies</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["💉 Vaccination", "🦟 Vector Control", "👥 Community & Personal"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("JE Vaccination Program")
            st.write("**Program:** Universal Immunization Programme (UIP)")
            st.write("**Vaccine:** Live attenuated SA 14-14-2")
            st.write("**Target:** Children aged 1-15 years")
            st.write("**Coverage:** High in UP, Bihar, Assam, West Bengal")
            st.write("**Effectiveness:** 95% protection")
            st.write("**Strategy:** Mass campaigns in endemic districts")

        with col2:
            st.subheader("Chikungunya Vaccination")
            st.write("**Status:** Emerging vaccines available")
            st.write("**Vaccines:** Ixchiq, Valneva (limited availability)")
            st.write("**Effectiveness:** 25% (vaccination not primary strategy)")
            st.write("**Focus:** Vector control and personal protection")
            st.write("**Research:** Ongoing development for better vaccines")

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("JE Vector Control")
            st.write("**Primary Vector:** Culex tritaeniorhynchus")
            st.write("**Strategies:**")
            st.write("• Fogging and larviciding (NVBDCP)")
            st.write("• Pig management in rural areas")
            st.write("• Rice field irrigation control")
            st.write("• Environmental management")
            st.write("**Effectiveness:** 85%")

        with col2:
            st.subheader("Chikungunya Vector Control")
            st.write("**Primary Vectors:** Aedes aegypti/albopictus")
            st.write("**Strategies:**")
            st.write("• Source reduction (weekly container emptying)")
            st.write("• Community education on waste management")
            st.write("• Larviciding and adulticiding")
            st.write("• Indoor residual spraying during outbreaks")
            st.write("**Effectiveness:** 95%")

    with tab3:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Personal Protection (JE)")
            st.write("**Measures:**")
            st.write("• Repellents containing DEET")
            st.write("• Long-sleeved clothing")
            st.write("• Bed nets (especially in rural areas)")
            st.write("• Avoid outdoor activities during peak hours")
            st.write("**Effectiveness:** 75%")

        with col2:
            st.subheader("Personal Protection (Chikungunya)")
            st.write("**Measures:**")
            st.write("• Repellents containing DEET")
            st.write("• Long-sleeved clothing")
            st.write("• Bed nets (day-biting mosquitoes)")
            st.write("• Screen doors and windows")
            st.write("• Avoid water storage in containers")
            st.write("**Effectiveness:** 85%")

    # Economic impact
    st.markdown('<h2 class="section-header">Economic Impact in India</h2>', unsafe_allow_html=True)

    if os.path.exists('economic_impact.png'):
        st.image('economic_impact.png', caption='Economic Impact Comparison (Annual Cost in ₹ Crores)', use_column_width=True)

    st.markdown("""
    <div class="info-box">
        <h3>💰 Key Economic Insights</h3>
        <ul>
            <li><strong>JE:</strong> ₹1000 crores annual cost (disability care, lost productivity)</li>
            <li><strong>Chikungunya:</strong> ₹500-760 crores per major outbreak</li>
            <li><strong>Both:</strong> Significant burden on healthcare system and economy</li>
            <li><strong>Prevention:</strong> More cost-effective than treatment and rehabilitation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "📈 Visualizations":
    st.markdown('<h1 class="main-header">Interactive Visualizations</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Disease Burden Visualizations</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("JE Cases by State")
        if os.path.exists('je_cases_india.png'):
            st.image('je_cases_india.png', caption='Japanese Encephalitis Cases by Indian State', use_column_width=True)

    with col2:
        st.subheader("Chikungunya Cases by State")
        if os.path.exists('chikungunya_cases_india.png'):
            st.image('chikungunya_cases_india.png', caption='Chikungunya Cases by Indian State', use_column_width=True)

    # Burden comparison
    st.markdown('<h2 class="section-header">Burden Comparison</h2>', unsafe_allow_html=True)

    if os.path.exists('burden_comparison.png'):
        st.image('burden_comparison.png', caption='Global Disease Burden Distribution', use_column_width=True)

    # Seasonal patterns
    st.markdown('<h2 class="section-header">Seasonal Patterns</h2>', unsafe_allow_html=True)

    if os.path.exists('seasonal_pattern.png'):
        st.image('seasonal_pattern.png', caption='Seasonal Pattern and Monsoon Correlation', use_column_width=True)

    st.markdown("""
    <div class="info-box">
        <h3>📊 Visualization Insights</h3>
        <ul>
            <li><strong>Monsoon Impact:</strong> Peak transmission during July-October for both diseases</li>
            <li><strong>Regional Variation:</strong> JE concentrated in eastern states, Chikungunya nationwide</li>
            <li><strong>Burden Distribution:</strong> JE has higher fatality but Chikungunya affects more people</li>
            <li><strong>Economic Cost:</strong> Both diseases impose significant financial burden on healthcare system</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "📝 Assessment":
    st.markdown('<h1 class="main-header">Assessment & Quiz</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">MCQ Quiz (18 Questions)</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>📋 Quiz Information</h3>
        <ul>
            <li><strong>Total Questions:</strong> 18 (5 basic, 5 intermediate, 5 advanced, 3 case-based)</li>
            <li><strong>Passing Score:</strong> 70% (12.6/18)</li>
            <li><strong>Time Limit:</strong> 30 minutes</li>
            <li><strong>Assessment Type:</strong> Formative assessment for community medicine rotation</li>
            <li><strong>Format:</strong> Available in HTML and Google Forms</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Quiz preview
    st.markdown('<h2 class="section-header">Sample Questions</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🧠 Basic Level", "🔬 Intermediate Level", "🏥 Case-based"])

    with tab1:
        st.subheader("Basic Level (Understanding)")
        st.write("**1. What is the primary vector for Japanese Encephalitis transmission in India?**")
        st.write("A) Aedes aegypti")
        st.write("B) **Culex tritaeniorhynchus** ✓")
        st.write("C) Anopheles stephensi")
        st.write("D) Mansonia species")

        st.write("**2. Which disease is characterized by chronic joint pain lasting months to years?**")
        st.write("A) Japanese Encephalitis")
        st.write("B) **Chikungunya** ✓")
        st.write("C) Dengue")
        st.write("D) Malaria")

    with tab2:
        st.subheader("Intermediate Level (Application)")
        st.write("**6. Which of the following is a dead-end host in JE transmission cycle?**")
        st.write("A) Pigs")
        st.write("B) Water birds")
        st.write("C) **Humans** ✓")
        st.write("D) Culex mosquitoes")

        st.write("**7. What is the typical incubation period for Chikungunya?**")
        st.write("A) 1-3 days")
        st.write("B) **4-8 days** ✓")
        st.write("C) 10-14 days")
        st.write("D) 15-21 days")

    with tab3:
        st.subheader("Case-based (Clinical Application)")
        st.write("**16. A 10-year-old child from rural Uttar Pradesh presents with high fever, headache, and seizures during monsoon season. What is the most likely diagnosis?**")
        st.write("A) Dengue fever")
        st.write("B) **Japanese Encephalitis** ✓")
        st.write("C) Chikungunya")
        st.write("D) Malaria")

        st.write("**17. A 35-year-old woman presents with acute onset fever and severe joint pain. She lives in an urban area with poor waste management. What preventive measures should be recommended?**")
        st.write("A) JE vaccination")
        st.write("B) **Source reduction and personal protection for Chikungunya** ✓")
        st.write("C) Malaria prophylaxis")
        st.write("D) Dengue vaccination")

    # Quiz access
    st.markdown('<h2 class="section-header">Access Complete Quiz</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background: #e8f4f8; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>📱 Interactive HTML Quiz</h3>
            <p>Complete quiz with immediate scoring</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open HTML Quiz", type="primary"):
            st.markdown("[Open MCQ Quiz](MCQ_Quiz.html)")

    with col2:
        st.markdown("""
        <div style="background: #fff3cd; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>📋 Google Forms Quiz</h3>
            <p>Online assessment with detailed analytics</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("*Google Forms integration available in teaching materials*")

elif page == "🎬 Video Content":
    st.markdown('<h1 class="main-header">Educational Video Content</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Complete Video Script (8-10 minutes)</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>🎬 Video Information</h3>
        <ul>
            <li><strong>Duration:</strong> 8-10 minutes</li>
            <li><strong>Target Audience:</strong> MBBS students and healthcare professionals</li>
            <li><strong>Style:</strong> Educational, engaging, with visual aids</li>
            <li><strong>Format:</strong> MP4 (compatible with most platforms)</li>
            <li><strong>Subtitles:</strong> English and Hindi</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Video script sections
    st.markdown('<h2 class="section-header">Video Script Preview</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎬 Introduction", "🦟 JE Section", "🦠 Chikungunya Section", "⚖️ Comparison", "🛡️ Prevention"])

    with tab1:
        st.subheader("Introduction (0:00 - 0:45)")
        st.write("""
        **Narrator:**
        "Welcome to this comprehensive educational video on Japanese Encephalitis and Chikungunya – two critical mosquito-borne diseases that every Indian medical student must understand. As future healthcare providers, you'll encounter these diseases in your practice, especially in rural and urban outbreak scenarios.

        Today, we'll explore their epidemiology, clinical features, diagnosis, treatment, and most importantly, prevention strategies tailored to the Indian context. This knowledge aligns with your CBME curriculum and will prepare you for real-world challenges in community medicine.

        Let's dive into the fascinating world of these arboviruses and understand why they remain significant public health challenges in India."
        """)

    with tab2:
        st.subheader("Section 1: Japanese Encephalitis (0:45 - 3:30)")
        st.write("""
        **Narrator:**
        "First, let's talk about Japanese Encephalitis, or JE. This flavivirus is transmitted primarily by the Culex tritaeniorhynchus mosquito and is endemic in 24 countries, putting over 3 billion people at risk globally.

        In India, JE is a major concern in states like Uttar Pradesh, Bihar, West Bengal, and Assam. The disease follows a seasonal pattern, peaking during monsoon months from July to October, when rice cultivation creates ideal breeding conditions for mosquitoes.

        **Key Epidemiology:**
        - Annual global cases: Approximately 100,000 clinical cases
        - Indian burden: 1,000-3,000 reported cases annually
        - Age group most affected: Children under 15 years
        - Case fatality rate: 20-30% for severe cases
        - Long-term sequelae: 30-50% of survivors develop neurological deficits"
        """)

    with tab3:
        st.subheader("Section 2: Chikungunya (3:30 - 5:45)")
        st.write("""
        **Narrator:**
        "Now, let's shift to Chikungunya – an alphavirus that has caused significant outbreaks in India and globally. Since its identification in Tanzania in 1952, CHIKV has spread to over 110 countries.

        In India, we've seen major outbreaks, notably the 2006 epidemic that affected over 1.3 million people across Kerala, Karnataka, Maharashtra, and Andhra Pradesh. More recently, the 2016-2017 outbreaks in Delhi and northern states highlighted the urban transmission potential.

        **Key Epidemiology:**
        - Global distribution: Africa, Asia, Americas, Europe
        - Indian outbreaks: All states affected, with major epidemics every few years
        - Age group affected: All ages, but adults often more symptomatic
        - Case fatality rate: Less than 0.1% (rarely fatal)
        - Chronic impact: 10-30% develop chronic arthritis"
        """)

    with tab4:
        st.subheader("Section 3: Comparative Analysis (5:45 - 7:00)")
        st.write("""
        **Narrator:**
        "Now, let's compare these two important diseases:

        **Similarities:**
        - Both are mosquito-borne viral diseases prevalent in India
        - Both show seasonal patterns linked to monsoon rains
        - Both are preventable through vector control and personal protection
        - Both require integrated disease surveillance through IDSP

        **Key Differences:**
        - JE affects the central nervous system with high fatality
        - Chikungunya causes severe joint pain with chronic morbidity
        - JE requires animal reservoirs while Chikungunya does not
        - Different vectors and control strategies needed"
        """)

    with tab5:
        st.subheader("Section 4: Prevention and Control (7:00 - 8:30)")
        st.write("""
        **Narrator:**
        "Prevention is the cornerstone of managing both diseases. Let's look at India-specific strategies:

        **For Japanese Encephalitis:**
        - Vaccination through Universal Immunization Programme using SA 14-14-2 vaccine
        - Target: Children aged 1-15 years in endemic districts
        - Vector control: Fogging, larviciding in rural areas
        - Surveillance: Acute Encephalitis Syndrome (AES) monitoring

        **For Chikungunya:**
        - Source reduction: Eliminating mosquito breeding sites
        - Community education: Weekly container emptying and cleaning
        - Personal protection: Repellents, long clothing, bed nets
        - Outbreak response: Indoor residual spraying and fogging"
        """)

    # Video production guidelines
    st.markdown('<h2 class="section-header">Video Production Guidelines</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px;">
        <h3>🎬 Production Requirements</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div>
                <h4>Visual Elements</h4>
                <ul>
                    <li>High-quality animations of transmission cycles</li>
                    <li>Maps showing disease distribution in India</li>
                    <li>Clinical symptom illustrations</li>
                    <li>Prevention strategy demonstrations</li>
                    <li>Real footage of vector control activities</li>
                </ul>
            </div>
            <div>
                <h4>Technical Specifications</h4>
                <ul>
                    <li>Resolution: 1080p HD</li>
                    <li>Format: MP4 (compatible with most platforms)</li>
                    <li>Subtitles: English and Hindi</li>
                    <li>Duration: 8-10 minutes for optimal engagement</li>
                    <li>Audio: Clear narration with educational background music</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "📚 Resources":
    st.markdown('<h1 class="main-header">Resources & References</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Comprehensive References (28 Sources)</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["🏛️ Government Sources", "🌍 International Sources", "📚 Scientific Literature", "🎓 Educational Resources"])

    with tab1:
        st.subheader("Indian Government Sources")
        st.write("**1-4: Primary Health Organizations**")
        st.write("• National Vector Borne Disease Control Programme (NVBDCP)")
        st.write("• Integrated Disease Surveillance Programme (IDSP)")
        st.write("• Universal Immunization Programme (UIP)")
        st.write("• Indian Council of Medical Research (ICMR)")

        st.write("**5-7: Policy Documents**")
        st.write("• NVBDCP Guidelines for Prevention and Control")
        st.write("• IDSP Weekly Outbreak Reports")
        st.write("• UIP Operational Guidelines for JE Vaccination")

    with tab2:
        st.subheader("International Sources")
        st.write("**1-2: World Health Organization**")
        st.write("• Japanese Encephalitis Fact Sheet (2024)")
        st.write("• Chikungunya Fact Sheet (2025)")

        st.write("**3-4: Centers for Disease Control**")
        st.write("• Japanese Encephalitis Guidelines")
        st.write("• Chikungunya Virus Information")

        st.write("**5: Global Health Observatory**")
        st.write("• Disease burden data and statistics")

    with tab3:
        st.subheader("Scientific Literature")
        st.write("**1-4: Key Research Papers**")
        st.write("• Quan et al. (2022) - Global epidemiology of chikungunya")
        st.write("• Wimalasiri-Yapa et al. (2019) - Chikungunya in Asia-Pacific")
        st.write("• Campbell et al. (2011) - Global incidence of JE")
        st.write("• Murhekar et al. (2017) - Burden of AES in India")

        st.write("**5-7: Indian Context Studies**")
        st.write("• Kakkar et al. (2012) - 2006 Chikungunya outbreak")
        st.write("• Phukan et al. (2016) - JE in India current status")
        st.write("• National Institute of Virology annual reports")

    with tab4:
        st.subheader("Educational Resources")
        st.write("**1-2: Medical Education**")
        st.write("• National Medical Commission CBME Curriculum")
        st.write("• Medical Council of India regulations")

        st.write("**3-4: Textbooks**")
        st.write("• Park's Textbook of Preventive and Social Medicine")
        st.write("• Harrison's Principles of Internal Medicine")

        st.write("**5: Online Resources**")
        st.write("• PubMed Central - Research articles")
        st.write("• Google Scholar - Academic publications")

    # Citation style
    st.markdown('<h2 class="section-header">Citation Style</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background: #e8f4f8; padding: 20px; border-radius: 10px;">
        <h3>📝 Vancouver Style (Medical Literature)</h3>
        <p>References are formatted according to Vancouver style commonly used in medical literature. For academic writing, students should follow the specific citation style recommended by their institution.</p>
        <p><strong>Example:</strong></p>
        <p>1. World Health Organization. Japanese Encephalitis Fact Sheet. Geneva: WHO; 2024.</p>
        <p>2. National Vector Borne Disease Control Programme. Guidelines for Prevention and Control of Japanese Encephalitis and Chikungunya. New Delhi: Ministry of Health and Family Welfare, Government of India; 2023.</p>
    </div>
    """, unsafe_allow_html=True)

    # Additional resources
    st.markdown('<h2 class="section-header">Additional Learning Resources</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Online Platforms")
        st.write("**📊 NVBDCP Dashboard**")
        st.write("Real-time surveillance data and outbreak reports")

        st.write("**📋 IDSP Portal**")
        st.write("Weekly disease surveillance and reporting")

        st.write("**🌍 WHO Global Health Observatory**")
        st.write("International disease burden and statistics")

        st.write("**📚 PubMed Central**")
        st.write("Research articles and systematic reviews")

    with col2:
        st.subheader("Educational Tools")
        st.write("**🎯 Google Forms Quiz**")
        st.write("Online assessment with detailed analytics")

        st.write("**📹 Educational Video**")
        st.write("8-10 minute comprehensive video script")

        st.write("**📊 Interactive Dashboard**")
        st.write("This Streamlit application for self-paced learning")

        st.write("**📖 Student Handouts**")
        st.write("Condensed study material for quick reference")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; padding: 20px;">
    <p><strong>JE & Chikungunya Teaching Dashboard</strong></p>
    <p>Comprehensive MBBS Teaching Material | CBME Aligned | National Medical Commission</p>
    <p>Developed for Indian Medical Education | Updated 2025</p>
    <p>📧 For questions or updates, refer to official sources in references section</p>
</div>
""", unsafe_allow_html=True)
