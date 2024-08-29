import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("my.jpeg", width=230)

with col2:
    st.title("LALIT TANWAR", anchor=False)
    st.write("Data Analyst, assisting enterprises by supporting data-driven decision-making.")
    st.write("TANWARLALIT@GMAIL.COM")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 0 to 1 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel, Power BI, SQL, Tableau
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Streamlit, Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, Tableau, MS Excel
    - Modeling: Logistic regression, multi linear regression, Classification
    - Databases: MySQL, SQL
    """
)

