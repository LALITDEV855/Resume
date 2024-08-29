import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "projects.py",
    title="Projects Dashboard",
    icon=":material/bar_chart:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Connect with ❤️ LinkedIn [LALIT](https://www.linkedin.com/in/lalit-tanwar-000219256/)")
st.sidebar.markdown("Connect with ❤️ GitHub [LALIT](https://github.com/LALITDEV855)")

# --- RUN NAVIGATION ---
pg.run()