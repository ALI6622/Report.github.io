import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data for the previous Sindh data
sindh_data = {
    'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23'],
    'Province': ['Sindh', 'Sindh', 'Sindh', 'Sindh', 'Sindh', 'Sindh', 'Sindh', 'Sindh'],
    'Total Live births': [7845, 7497, 8761, 7232, 8447, 8944, 10460, 12570],
    'Total Vaccinated with OPV': [7298, 7058, 8282, 6849, 8107, 8251, 9993, 11948]
}

sindh_df = pd.DataFrame(sindh_data)

# Calculate the percentage vaccinated against live birth for Sindh
sindh_df['Percentage Vaccinated'] = (sindh_df['Total Vaccinated with OPV'] / sindh_df['Total Live births']) * 100

# Data for the new "Birth Dose" initiative in KPK (Peshawar)
kpk_data = {
    'Initiative': ['Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose'],
    'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23'],
    'Province': ['KPK', 'KPK', 'KPK', 'KPK', 'KPK', 'KPK', 'KPK', 'KPK'],
    'Total Live births': [5535, 4806, 4763, 4680, 4693, 4733, 5007, 5121],
    'Total Vaccinated with OPV': [5262, 4416, 4423, 4214, 4533, 4541, 4812, 4927]
}

kpk_df = pd.DataFrame(kpk_data)

# Calculate the percentage vaccinated against live birth for KPK (Peshawar)
kpk_df['Percentage Vaccinated'] = (kpk_df['Total Vaccinated with OPV'] / kpk_df['Total Live births']) * 100

# Data for the new "Birth Dose" initiative in GB (Gilgit-Baltistan)
gb_data = {
    'Initiative': ['Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose'],
    'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23'],
    'Province': ['GB', 'GB', 'GB', 'GB', 'GB', 'GB', 'GB', 'GB'],
    'Total Live births': [1232, 1213, 1332, 1543, 1106, 1370, 1291, 1218],
    'Total Vaccinated with OPV': [1211, 1201, 1302, 1335, 1091, 1345, 1268, 1207]
}

gb_df = pd.DataFrame(gb_data)

# Calculate the percentage vaccinated against live birth for GB (Gilgit-Baltistan)
gb_df['Percentage Vaccinated'] = (gb_df['Total Vaccinated with OPV'] / gb_df['Total Live births']) * 100

# Data for the new "Birth Dose" initiative in Balochistan
balochistan_data = {
    'Initiative': ['Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose'],
    'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23'],
    'Province': ['Balochistan', 'Balochistan', 'Balochistan', 'Balochistan', 'Balochistan', 'Balochistan', 'Balochistan', 'Balochistan'],
    'Total Live births': [4701, 4258, 4927, 3897, 4520, 4025, 4370, 5104],
    'Total Vaccinated with OPV': [4520, 4165, 4775, 3742, 4489, 3874, 4154, 4786]
}

balochistan_df = pd.DataFrame(balochistan_data)

# Calculate the percentage vaccinated against live birth for Balochistan
balochistan_df['Percentage Vaccinated'] = (balochistan_df['Total Vaccinated with OPV'] / balochistan_df['Total Live births']) * 100

# Data for the new "Birth Dose" initiative in AJK (Azad Jammu and Kashmir)
ajk_data = {
    'Initiative': ['Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose', 'Birth Dose'],
    'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23'],
    'Province': ['AJK', 'AJK', 'AJK', 'AJK', 'AJK', 'AJK', 'AJK', 'AJK'],
    'Total Live births': [3123, 2907, 2881, 2517, 2743, 2416, 2732, 2855],
    'Total Vaccinated with OPV': [3024, 2791, 2821, 2458, 2692, 2346, 2683, 2809]
}

ajk_df = pd.DataFrame(ajk_data)

# Calculate the percentage vaccinated against live birth for AJK (Azad Jammu and Kashmir)
ajk_df['Percentage Vaccinated'] = (ajk_df['Total Vaccinated with OPV'] / ajk_df['Total Live births']) * 100

# Streamlit app
st.title("24/7 Outreach Report")
st.write("Vaccination Percentage against Live Birth")

# Display data table for Sindh
st.subheader("Data Table - Sindh")
st.dataframe(sindh_df)

# Create and display the 2D column chart for Sindh
st.subheader("Sindh Vaccination Chart")
fig_sindh, ax_sindh = plt.subplots(figsize=(10, 6))
ax_sindh.bar(sindh_df['Month'], sindh_df['Percentage Vaccinated'], color='skyblue')

# Add label values on the chart for Sindh
for i, val in enumerate(sindh_df['Percentage Vaccinated']):
    ax_sindh.text(i, val + 1, f'{val:.2f}%', ha='center', va='bottom', fontsize=10)

ax_sindh.set_xlabel("Month")
ax_sindh.set_ylabel("Percentage Vaccinated")
ax_sindh.set_title("Percentage of Vaccinated Live Births in Sindh (2023)")
plt.xticks(rotation=45)
plt.ylim(0, 140)  # Adjust the y-axis limits as needed

# Display the chart for Sindh using st.pyplot
st.pyplot(fig_sindh)

# Display data table for KPK (Peshawar)
st.subheader("Data Table - KPK")
st.dataframe(kpk_df)

# Create and display the 2D column chart for KPK (Peshawar)
st.subheader("KPK Vaccination Chart")
fig_kpk, ax_kpk = plt.subplots(figsize=(10, 6))
ax_kpk.bar(kpk_df['Month'], kpk_df['Percentage Vaccinated'], color='lightgreen')

# Add label values on the chart for KPK (Peshawar)
for i, val in enumerate(kpk_df['Percentage Vaccinated']):
    ax_kpk.text(i, val + 1, f'{val:.2f}%', ha='center', va='bottom', fontsize=10)

ax_kpk.set_xlabel("Month")
ax_kpk.set_ylabel("Percentage Vaccinated")
ax_kpk.set_title("Percentage of Vaccinated Live Births in KPK (Peshawar) (2023)")
plt.xticks(rotation=45)
plt.ylim(0, 140)  # Adjust the y-axis limits as needed

# Display the chart for KPK (Peshawar) using st.pyplot
st.pyplot(fig_kpk)

# Display data table for GB (Gilgit-Baltistan)
st.subheader("Data Table - GB")
st.dataframe(gb_df)

# Create and display the 2D column chart for GB (Gilgit-Baltistan)
st.subheader("GB Vaccination Chart")
fig_gb, ax_gb = plt.subplots(figsize=(10, 6))
ax_gb.bar(gb_df['Month'], gb_df['Percentage Vaccinated'], color='lightcoral')

# Add label values on the chart for GB (Gilgit-Baltistan)
for i, val in enumerate(gb_df['Percentage Vaccinated']):
    ax_gb.text(i, val + 1, f'{val:.2f}%', ha='center', va='bottom', fontsize=10)

ax_gb.set_xlabel("Month")
ax_gb.set_ylabel("Percentage Vaccinated")
ax_gb.set_title("Percentage of Vaccinated Live Births in GB (Gilgit-Baltistan) (2023)")
plt.xticks(rotation=45)
plt.ylim(0, 140)  # Adjust the y-axis limits as needed

# Display the chart for GB (Gilgit-Baltistan) using st.pyplot
st.pyplot(fig_gb)

# Display data table for Balochistan
st.subheader("Data Table - Balochistan")
st.dataframe(balochistan_df)

# Create and display the 2D column chart for Balochistan
st.subheader("Balochistan Vaccination Chart")
fig_balochistan, ax_balochistan = plt.subplots(figsize=(10, 6))
ax_balochistan.bar(balochistan_df['Month'], balochistan_df['Percentage Vaccinated'], color='gold')

# Add label values on the chart for Balochistan
for i, val in enumerate(balochistan_df['Percentage Vaccinated']):
    ax_balochistan.text(i, val + 1, f'{val:.2f}%', ha='center', va='bottom', fontsize=10)

ax_balochistan.set_xlabel("Month")
ax_balochistan.set_ylabel("Percentage Vaccinated")
ax_balochistan.set_title("Percentage of Vaccinated Live Births in Balochistan (2023)")
plt.xticks(rotation=45)
plt.ylim(0, 140)  # Adjust the y-axis limits as needed

# Display the chart for Balochistan using st.pyplot
st.pyplot(fig_balochistan)

# Display data table for AJK (Azad Jammu and Kashmir)
st.subheader("Data Table - AJK")
st.dataframe(ajk_df)

# Create and display the 2D column chart for AJK (Azad Jammu and Kashmir)
st.subheader("AJK  Vaccination Chart")
fig_ajk, ax_ajk = plt.subplots(figsize=(10, 6))
ax_ajk.bar(ajk_df['Month'], ajk_df['Percentage Vaccinated'], color='lightblue')

# Add label values on the chart for AJK (Azad Jammu and Kashmir)
for i, val in enumerate(ajk_df['Percentage Vaccinated']):
    ax_ajk.text(i, val + 1, f'{val:.2f}%', ha='center', va='bottom', fontsize=10)

ax_ajk.set_xlabel("Month")
ax_ajk.set_ylabel("Percentage Vaccinated")
ax_ajk.set_title("Percentage of Vaccinated Live Births in AJK (Azad Jammu and Kashmir) (2023)")
plt.xticks(rotation=45)
plt.ylim(0, 140)  # Adjust the y-axis limits as needed

# Display the chart for AJK (Azad Jammu and Kashmir) using st.pyplot
st.pyplot(fig_ajk)

# Hide Streamlit footer by adding custom CSS
hide_footer_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)
