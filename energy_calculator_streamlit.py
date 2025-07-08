import streamlit as st
# import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Energy Consumption Calculator",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #FF6B35;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .result-box {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E8B57;
        margin: 20px 0;
    }
    .cost-highlight {
        font-size: 1.8rem;
        color: #FF6B35;
        font-weight: bold;
    }
    .energy-highlight {
        font-size: 1.5rem;
        color: #2E8B57;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">⚡ Energy Consumption Calculator</h1>', unsafe_allow_html=True)

# Sidebar for user information
st.sidebar.header("📋 Personal Information")
name = st.sidebar.text_input("Enter your name:", placeholder="Your Name")
age = st.sidebar.number_input("Enter your age:", min_value=1, max_value=120, value=25)
city = st.sidebar.text_input("Enter your city:", placeholder="Your City")
area = st.sidebar.text_input("Enter your area:", placeholder="Your Area")

# Main content area
st.markdown('<h2 class="section-header">🏠 Appliance Information</h2>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Appliances")
    light = st.number_input("Number of Lights:", min_value=0, value=0, step=1)
    fans = st.number_input("Number of Fans:", min_value=0, value=0, step=1)
    tv = st.number_input("Number of TVs:", min_value=0, value=0, step=1)

with col2:
    st.subheader("Major Appliances")
    
    # AC section
    has_ac = st.checkbox("Do you have an AC?")
    ac = 0
    if has_ac:
        ac = st.number_input("Number of ACs:", min_value=0, value=1, step=1)
    
    # Fridge section
    has_fridge = st.checkbox("Do you have a Fridge?")
    fridge = 0
    if has_fridge:
        fridge = st.number_input("Number of Fridges:", min_value=0, value=1, step=1)
    
    # Washing Machine section
    has_wm = st.checkbox("Do you have a Washing Machine?")
    wm = 0
    if has_wm:
        wm = st.number_input("Number of Washing Machines:", min_value=0, value=1, step=1)

# Energy consumption rates (kWh per day)
energy_rates = {
    "light": 0.2,
    "fans": 0.2,
    "tv": 0.3,
    "ac": 3.0,
    "fridge": 3.1,
    "wm": 2.8
}

# Calculate energy consumption
cal_energy = 0
cal_energy += light * energy_rates["light"]
cal_energy += fans * energy_rates["fans"]
cal_energy += tv * energy_rates["tv"]
cal_energy += ac * energy_rates["ac"]
cal_energy += fridge * energy_rates["fridge"]
cal_energy += wm * energy_rates["wm"]

# Calculate cost
rate_per_unit = 8.0
total_cost = round(cal_energy * rate_per_unit, 2)

# Display results
if st.button("Calculate Energy Consumption", type="primary"):
    if name and city and area:
        st.markdown('<h2 class="section-header">📊 Results</h2>', unsafe_allow_html=True)
        
        # Results in a nice box
        st.markdown(f"""
        <div class="result-box">
            <h3>👤 Personal Details</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Age:</strong> {age}</p>
            <p><strong>City:</strong> {city}</p>
            <p><strong>Area:</strong> {area}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Appliances breakdown
        st.markdown("### 🔌 Appliances Breakdown")
        appliance_data = {
            "Appliance": ["Lights", "Fans", "TVs", "ACs", "Fridges", "Washing Machines"],
            "Count": [light, fans, tv, ac, fridge, wm],
            "Energy (kWh/day)": [
                round(light * energy_rates["light"], 2),
                round(fans * energy_rates["fans"], 2),
                round(tv * energy_rates["tv"], 2),
                round(ac * energy_rates["ac"], 2),
                round(fridge * energy_rates["fridge"], 2),
                round(wm * energy_rates["wm"], 2)
            ]
        }
        
        st.table(appliance_data)
        
        # Total consumption and cost
        st.markdown(f"""
        <div class="result-box">
            <p class="energy-highlight">Total Energy Consumption: {cal_energy} kWh/day</p>
            <p class="cost-highlight">Total Daily Cost: ₹{total_cost}</p>
            <p><strong>Monthly Cost (approx):</strong> ₹{round(total_cost * 30, 2)}</p>
            <p><strong>Annual Cost (approx):</strong> ₹{round(total_cost * 365, 2)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Energy saving tips
        st.markdown("### 💡 Energy Saving Tips")
        tips = [
            "Switch to LED bulbs to reduce lighting energy consumption",
            "Use ceiling fans instead of AC when possible",
            "Set AC temperature to 24°C or higher",
            "Regular maintenance of appliances improves efficiency",
            "Unplug devices when not in use to avoid phantom loads"
        ]
        
        for tip in tips:
            st.write(f"• {tip}")
            
    else:
        st.error("Please fill in all personal information fields (Name, City, Area)")

# Additional information in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Energy Rates Used")
st.sidebar.markdown("""
- **Lights:** 0.2 kWh/day each
- **Fans:** 0.2 kWh/day each  
- **TVs:** 0.3 kWh/day each
- **ACs:** 3.0 kWh/day each
- **Fridges:** 3.1 kWh/day each
- **Washing Machines:** 2.8 kWh/day each

**Rate:** ₹8.0 per kWh
""")

# Footer
st.markdown("---")
st.markdown("*Note: These are approximate values. Actual consumption may vary based on usage patterns and appliance efficiency.*")