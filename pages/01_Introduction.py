import streamlit as st
from common import inject_css

inject_css()
st.markdown('<h2 class="section-title">📖 Introduction</h2>', unsafe_allow_html=True)
    
st.markdown("""
### What is ECB Mode?
    
**Electronic Code Book (ECB)** is the simplest block cipher mode of operation. In ECB mode, 
each block of plaintext is encrypted independently using the same key, producing a corresponding 
block of ciphertext.
    
### Key Characteristics:
    
- **Deterministic**: Identical plaintext blocks produce identical ciphertext blocks
- **Parallel Processing**: Each block can be encrypted/decrypted independently
- **Block-by-Block Operation**: Processes data in fixed-size blocks (128 bits for AES)
    
### Where is ECB Used?
    
While ECB has significant security limitations, it finds use in specific scenarios:
    
1. **Random Data Encryption**: When encrypting truly random data where patterns don't matter
2. **Single Block Encryption**: Encrypting data that fits in a single block
3. **Key Wrapping**: In some key encryption scenarios (though other modes are preferred)
4. **Educational Purposes**: Demonstrating basic encryption concepts
""")
