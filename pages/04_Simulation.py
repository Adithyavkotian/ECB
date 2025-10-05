import streamlit as st
from common import inject_css, encrypt_aes_ecb, decrypt_aes_ecb
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

inject_css()

st.markdown('<h2 class="section-title">🧪 Simulation - AES ECB Encryption/Decryption</h2>', unsafe_allow_html=True)
st.markdown("### Try AES-ECB Encryption and Decryption")

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
plaintext = st.text_area("Enter plaintext to encrypt:", height=100, placeholder="Type your message here...")

if st.button("🔐 Encrypt") and key is not None:
    if plaintext:
        try:
            ciphertext_hex = encrypt_aes_ecb(plaintext, key)
            st.session_state.ciphertext = ciphertext_hex

            st.success("Encryption successful!")
            st.markdown("**Ciphertext (Hex):**")
            st.code(ciphertext_hex, language="text")
            st.info(f"Original length: {len(plaintext)} bytes | Encrypted length: {len(bytes.fromhex(ciphertext_hex))} bytes")
        except Exception as e:
            st.error(f"Encryption error: {str(e)}")
    else:
        st.warning("Please enter plaintext to encrypt!")

st.markdown("---")

# Decryption Section
st.markdown("### 🔓 Decryption")
if 'ciphertext' in st.session_state:
    ciphertext_input = st.text_area("Ciphertext (Hex):", value=st.session_state.ciphertext, height=100)
else:
    ciphertext_input = st.text_area("Enter ciphertext (Hex) to decrypt:", height=100, placeholder="Paste Hex encoded ciphertext here...")

if st.button("🔓 Decrypt") and key is not None:
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

# ECB Demo Section
with st.expander("🎯 See ECB Pattern Demonstration"):
    st.markdown("""
    **ECB Mode Weakness Demo:**
    Enter a repetitive text like "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" (32 A's).
    Only the blocks corresponding to your plaintext are shown (padding is excluded from block display).
    This demonstrates why ECB is **not secure** for repeated plaintext blocks.
    """)
    demo_text = st.text_input("Try this:", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")  # 32 A's

    if st.button("Encrypt Demo Text") and key is not None:
        if demo_text:
            plaintext_bytes = demo_text.encode('utf-8')
            if len(plaintext_bytes) % AES.block_size != 0:
                st.warning(f"Input length is {len(plaintext_bytes)} bytes, which is not a multiple of 16. "
                           "Please enter a length divisible by 16 for this demo.")
            else:
                # Encrypt WITHOUT padding for demonstration
                cipher = AES.new(key, AES.MODE_ECB)
                ciphertext_bytes = cipher.encrypt(plaintext_bytes)
                cipher_hex = ciphertext_bytes.hex()

                # Split into 16-byte (32 hex chars) blocks
                block_size_hex = AES.block_size * 2
                blocks = [cipher_hex[i:i+block_size_hex] for i in range(0, len(cipher_hex), block_size_hex)]

                for idx, block in enumerate(blocks, start=1):
                    st.markdown(f"**Block {idx}:**")
                    st.code(block, language="text")

                st.markdown("**Full Ciphertext (Hex):**")
                st.code(cipher_hex, language="text")
                st.info("👉 Notice: identical plaintext blocks produce identical ciphertext blocks in ECB mode!")
