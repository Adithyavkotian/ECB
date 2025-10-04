import streamlit as st
from common import inject_css

inject_css()
st.markdown('<h2 class="section-title">📝 Procedure</h2>', unsafe_allow_html=True)
    
st.markdown("""### Step-by-Step Guide to Run AES-ECB Encryption/Decryption""")

st.markdown("""#### 🔧 Prerequisites""")
st.code('''
# Install required library
pip install pycryptodome streamlit
''', language="bash")

st.markdown("""#### 📋 Step 1: Setup and Key Generation""")
st.markdown("""
1. Navigate to the **Simulation** page
2. Choose between:
   - **Generate Random Key**: Automatically creates a secure 128-bit key
   - **Enter Custom Key**: Input your own 32-character hexadecimal key
3. If using random generation, click "Generate New Key" to create a key
4. Note down the key (in hex format) for future use
""")

st.markdown("""#### 🔒 Step 2: Encryption Process""")
st.markdown("""
1. In the **Encryption** section, enter your plaintext message in the text area
2. Click the **"🔐 Encrypt"** button
3. The application will:
   - Apply PKCS7 padding to your message
   - Encrypt each 16-byte block using AES in ECB mode
   - Encode the result in Base64 format
4. Copy the displayed ciphertext for decryption
""")

st.markdown("""#### 🔓 Step 3: Decryption Process""")
st.markdown("""
1. In the **Decryption** section, paste the Base64-encoded ciphertext
2. Ensure you're using the **same key** that was used for encryption
3. Click the **"🔓 Decrypt"** button
4. The application will:
   - Decode the Base64 string
   - Decrypt each block using the same key
   - Remove PKCS7 padding
   - Display the original plaintext
""")

st.markdown("""#### 🎯 Step 4: Understanding ECB Patterns""")
st.markdown("""
1. Expand the **"ECB Pattern Demonstration"** section
2. Try encrypting repetitive text (e.g., "HELLO HELLO HELLO")
3. Observe how identical plaintext patterns appear in the ciphertext
4. This demonstrates the main security weakness of ECB mode
""")

st.markdown("---")

st.markdown("""### 💻 Code Implementation Example""")
st.code('''
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Generate a random 128-bit key
key = get_random_bytes(16)

# Encryption
def encrypt_aes_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(ciphertext).decode('utf-8')

# Decryption
def decrypt_aes_ecb(ciphertext_b64, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext_b64)
    decrypted_padded = cipher.decrypt(ciphertext)
    decrypted_data = unpad(decrypted_padded, AES.block_size)
    return decrypted_data.decode('utf-8')

# Example usage
plaintext = "Hello, World!"
ciphertext = encrypt_aes_ecb(plaintext, key)
decrypted = decrypt_aes_ecb(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
''', language='python')

st.markdown('''---''')

st.markdown("""### ⚠️ Important Notes""")
st.markdown("""
- **Key Management**: Keep your encryption key secure. Anyone with the key can decrypt your data.
- **Same Key Required**: Decryption requires the exact same key used for encryption.
- **Base64 Encoding**: Ciphertext is Base64-encoded for easy copying and display.
- **Padding**: Automatic PKCS7 padding is applied, so any length of input is supported.
- **ECB Limitations**: Remember that ECB mode reveals patterns. Use other modes (CBC, GCM) for production.
""")
