import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


def inject_css():
    st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .section-title {
        color: #2c3e50;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 10px;
        margin-top: 20px;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 15px;
        border-left: 5px solid #ffc107;
        border-radius: 5px;
        margin: 10px 0;
    }
    .home-container {
        background-color: #1a1d23;
        padding: 60px 40px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
    }
    .home-title {
        font-size: 3.5em;
        font-weight: bold;
        margin-bottom: 40px;
        color: white;
        line-height: 1.2;
    }
    .home-subtitle {
        font-size: 1.3em;
        margin-bottom: 30px;
        color: #e0e0e0;
    }
    .home-list {
        font-size: 1.2em;
        line-height: 2.5;
        color: #e0e0e0;
        margin-left: 20px;
    }
    .home-list li {
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)


def encrypt_aes_ecb(plaintext, key):
    """Encrypt plaintext using AES in ECB mode"""
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(ciphertext).decode('utf-8')


def decrypt_aes_ecb(ciphertext_b64, key):
    """Decrypt ciphertext using AES in ECB mode"""
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext_b64)
    decrypted_padded = cipher.decrypt(ciphertext)
    decrypted_data = unpad(decrypted_padded, AES.block_size)
    return decrypted_data.decode('utf-8')
