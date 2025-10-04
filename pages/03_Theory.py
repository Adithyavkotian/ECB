import streamlit as st
from common import inject_css

inject_css()
st.markdown('<h2 class="section-title">📚 Theory</h2>', unsafe_allow_html=True)

st.markdown("""### 🔑 Block Cipher & AES""")
st.markdown("""
A **block cipher** is a symmetric encryption algorithm that encrypts data in fixed-size blocks.  
**AES (Advanced Encryption Standard)** is the most widely used block cipher today.

- **Block Size**: 128 bits (16 bytes)  
- **Key Sizes**: 128, 192, or 256 bits  
- **Nature**: Symmetric (same key for encryption and decryption)  
- **Operations**: Multiple rounds of substitution, permutation, and mixing

AES has replaced the older DES standard due to its stronger security and efficiency.
""")

st.markdown("---")

st.markdown("""### 📦 Electronic Code Book (ECB) Mode""")
st.markdown("""
**ECB (Electronic Code Book)** is the simplest mode of operation for block ciphers.

**Working Principle:**
Each plaintext block is encrypted independently with the same key:

```
C₁ = E(K, P₁)  
C₂ = E(K, P₂)  
C₃ = E(K, P₃) ...
```

Where:  
- `Pᵢ` = Plaintext block i  
- `Cᵢ` = Ciphertext block i  
- `K` = Secret key  
- `E` = Encryption function
""")

st.markdown("---")

st.markdown("""### 🔧 Padding (PKCS7)""")
st.markdown("""
AES works only on blocks of **16 bytes**. If the message length is not a multiple of 16, padding is added.  
**PKCS7 Padding** is commonly used.

Example:  
If 5 bytes are missing to complete the block, add `05 05 05 05 05`.

**Padding Removal**:  
- Look at the last byte value (N).  
- Remove the last N bytes.  
""")

st.markdown("---")

st.markdown("""### 🔹 AES-ECB Functions in Python""")
st.code("""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Encrypt function
def encrypt_aes_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded)
    return base64.b64encode(ciphertext).decode()

# Decrypt function
def decrypt_aes_ecb(ciphertext_b64, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext_b64)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()
""", language="python")

st.markdown("""
**Explanation:**  
- `AES.new(key, AES.MODE_ECB)`: Creates AES cipher in ECB mode  
- `pad()`: Ensures message length is multiple of 16  
- `encrypt()`: Encrypts each block independently  
- `base64`: Encodes binary ciphertext into readable text  
- `unpad()`: Removes PKCS7 padding after decryption  
""")
