import streamlit as st
from common import inject_css

st.set_page_config(page_title="ECB Block Cipher Mode", page_icon="🔐", layout="wide")
inject_css()

st.title("Implement Block Cipher Mode: ECB (Electronic Code Book)")
st.markdown("""
Welcome to the **Implement Block Cipher Mode: ECB (Electronic Code Book)** project.

Use the left sidebar to navigate through the sections:
""")

st.markdown("""
- Introduction
- Objective
- Theory
- Simulation
- Procedure
- Conclusion
""")
