import streamlit as st
from common import inject_css

inject_css()
st.markdown('<h2 class="section-title">🎯 Objective</h2>', unsafe_allow_html=True)
    
st.markdown("""
### Objective
    
The goal of this assignment is to **implement and demonstrate AES encryption in ECB mode**.
    
### Key Points:
- Understand block cipher operation and ECB mode  
- Perform AES-ECB encryption and decryption with proper padding  
- Explore security limitations of ECB mode  
- Build a simple interactive demonstration for learning purposes
""")
