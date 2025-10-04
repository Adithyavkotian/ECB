import streamlit as st
from common import inject_css

inject_css()
st.markdown('<h2 class="section-title">🎓 Conclusion</h2>', unsafe_allow_html=True)
    
st.markdown("""
### Summary
    
In this assignment, we implemented the **AES algorithm in ECB mode** with PKCS7 padding. 
We successfully performed both encryption and decryption, gaining practical understanding 
of block cipher operations.
    
### Key Points
    
- ECB is simple but insecure for real-world use as it reveals patterns in data.  
- The exercise helped us understand encryption, padding, and symmetric key usage.  
- Safer modes like CBC, CTR, or GCM should be used in practice.  
""")

st.markdown('''---''')
