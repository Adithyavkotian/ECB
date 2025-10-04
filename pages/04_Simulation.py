import streamlit as st
from common import inject_css, encrypt_aes_ecb, decrypt_aes_ecb
from Crypto.Random import get_random_bytes
import base64

inject_css()

st.markdown('<h2 class="section-title">🧪 Simulation - AES ECB Encryption/Decryption</h2>', unsafe_allow_html=True)
    
st.markdown("""### Try AES-ECB Encryption and Decryption""")
    
# Key generation or input
col1, col2 = st.columns([2, 1])
    
with col1:
    key_option = st.radio("Key Selection:", ["Generate Random Key", "Enter Custom Key (Hex)"])
    
if key_option == "Generate Random Key":
    if 'aes_key' not in st.session_state:
        st.session_state.aes_key = get_random_bytes(16)
    
    if st.button("🔄 Generate New Key"):
        st.session_state.aes_key = get_random_bytes(16)
    
    key = st.session_state.aes_key
    st.code(f"Key (Hex): {key.hex()}", language="text")
else:
    key_input = st.text_input("Enter 128-bit Key (32 hex characters):", "")
    if key_input and len(key_input) == 32:
        try:
            key = bytes.fromhex(key_input)
        except:
            st.error("Invalid hex string!")
            key = None
    else:
        st.warning("Please enter exactly 32 hexadecimal characters (16 bytes)")
        key = None
    
st.markdown("---")
    
# Encryption Section
st.markdown("### 🔒 Encryption")
plaintext = st.text_area("Enter plaintext to encrypt:", height=100, 
                         placeholder="Type your message here...")
    
if st.button("🔐 Encrypt", type="primary") and key is not None:
    if plaintext:
        try:
            ciphertext = encrypt_aes_ecb(plaintext, key)
            st.session_state.ciphertext = ciphertext
            
            st.success("Encryption successful!")
            st.markdown("**Ciphertext (Base64):**")
            st.code(ciphertext, language="text")
            
            st.info(f"Original length: {len(plaintext)} bytes | "
                   f"Encrypted length: {len(base64.b64decode(ciphertext))} bytes")
        except Exception as e:
            st.error(f"Encryption error: {str(e)}")
    else:
        st.warning("Please enter plaintext to encrypt!")
    
st.markdown("---")
    
# Decryption Section
st.markdown("### 🔓 Decryption")
    
if 'ciphertext' in st.session_state:
    ciphertext_input = st.text_area("Ciphertext (Base64):", 
                                   value=st.session_state.ciphertext, 
                                   height=100)
else:
    ciphertext_input = st.text_area("Enter ciphertext (Base64) to decrypt:", height=100,
                                   placeholder="Paste Base64 encoded ciphertext here...")
    
if st.button("🔓 Decrypt", type="primary") and key is not None:
    if ciphertext_input:
        try:
            decrypted_text = decrypt_aes_ecb(ciphertext_input, key)
            
            st.success("Decryption successful!")
            st.markdown("**Decrypted plaintext:**")
            st.code(decrypted_text, language="text")
        except Exception as e:
            st.error(f"Decryption error: {str(e)}")
    else:
        st.warning("Please enter ciphertext to decrypt!")
    
st.markdown("---")
    
# Demo section
with st.expander("🎯 See ECB Pattern Demonstration"):
    st.markdown("""
    **ECB Mode Weakness Demo:**
    
    Try encrypting repetitive text like "AAAA AAAA AAAA AAAA" to see how identical 
    plaintext blocks produce identical ciphertext blocks. This demonstrates why ECB 
    is not secure for most applications.
    """)
        
    demo_text = st.text_input("Try this:", "HELLO HELLO HELLO HELLO")
    if st.button("Encrypt Demo Text") and key is not None:
        if demo_text:
            demo_cipher = encrypt_aes_ecb(demo_text, key)
            st.code(demo_cipher, language="text")
            st.info("Notice the patterns if you encrypt the same text multiple times!")
