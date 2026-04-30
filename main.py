import streamlit as st

st.set_page_config(page_title="Ruang Data", layout="centered")

# Header
st.title(" Ruang Data")
st.subheader("Pahami Data Tanpa Ribet")

st.write("""
Kami membantu mahasiswa dan UMKM memahami,
mengolah, dan menganalisis data secara praktis.
""")

# Layanan
st.header("💼 Layanan Kami")

st.markdown("""
- Konsultasi Data
- Analisis & Visualisasi
- Pembuatan Dashboard (Excel / Power BI)
- Insight & Rekomendasi
""")

# Paket
st.header(" Paket Harga")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Mahasiswa")
    st.write("Rp 150k")
    
with col2:
    st.subheader("UMKM")
    st.write("Rp 300k")

with col3:
    st.subheader("Dashboard")
    st.write("Rp 500k")

# CTA
st.header("📞 Konsultasi Sekarang")

st.markdown("[Klik WhatsApp](https://wa.me/628xxxx)")
