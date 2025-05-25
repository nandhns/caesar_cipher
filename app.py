# app.py

import streamlit as st
import sqlite3
from datetime import datetime
from caesar import caesar_encrypt, caesar_decrypt

# --- DB Setup ---
DB_NAME = "database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original TEXT,
            encrypted TEXT,
            shift INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- Page Title ---
st.title("🔐 Caesar Cipher Encryptor")

# --- User Input Form ---
with st.form("encrypt_form"):
    plaintext = st.text_area("Enter your plaintext message:")
    shift = st.slider("Choose shift (1–25)", 1, 25, 3)
    submitted = st.form_submit_button("Encrypt and Save")

    if submitted:
        encrypted = caesar_encrypt(plaintext, shift)
        st.success("Message encrypted!")
        st.text_area("🔒 Encrypted Message:", value=encrypted, height=100)

        # Save to DB
        conn = sqlite3.connect(DB_NAME)
        conn.execute("INSERT INTO messages (original, encrypted, shift) VALUES (?, ?, ?)",
                     (plaintext, encrypted, shift))
        conn.commit()
        conn.close()

# --- Display Saved Messages ---
st.subheader("📜 Stored Messages")

conn = sqlite3.connect(DB_NAME)
rows = conn.execute("SELECT id, original, encrypted, shift, timestamp FROM messages ORDER BY id DESC").fetchall()
conn.close()

if rows:
    for row in rows:
        msg_id, original, encrypted, shift, timestamp = row
        with st.expander(f"🧾 Message ID {msg_id} | Shift: {shift} | Saved: {timestamp}"):
            st.code(f"Original: {original}\nEncrypted: {encrypted}", language="text")
            if st.button(f"🔓 Decrypt ID {msg_id}", key=f"decrypt_{msg_id}"):
                decrypted = caesar_decrypt(encrypted, shift)
                st.success(f"Decrypted Message: {decrypted}")
else:
    st.info("No messages stored yet.")
