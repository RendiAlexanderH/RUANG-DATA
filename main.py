import streamlit as st

# CONFIG
st.set_page_config(page_title="Ruang Data", layout="wide")

# BACKGROUND + STYLE
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1551288049-bebda4e38f71");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

.block-container {
    background: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 15px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# HERO SECTION
st.title("📊 Ruang Data")
st.subheader("Pahami Data Tanpa Ribet")

st.write("""
Kami membantu mahasiswa dan UMKM memahami,
mengolah, dan menganalisis data secara praktis dan mudah dipahami.
""")

st.markdown("### 🚀 Mulai sekarang, ubah data jadi keputusan!")

st.markdown("[👉 Konsultasi Sekarang (WhatsApp)](https://wa.me/628xxxx)")

st.divider()

# LAYANAN
st.header("💼 Layanan Kami")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ✅ Konsultasi Data  
    ✅ Analisis & Visualisasi  
    """)

with col2:
    st.markdown("""
    ✅ Dashboard (Excel / Power BI)  
    ✅ Insight & Rekomendasi  
    """)

st.divider()

# PAKET
st.header("💰 Paket Harga")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎓 Mahasiswa")
    st.write("Rp 150.000")
    st.write("✔ Skripsi\n✔ Tugas\n✔ Analisis sederhana")

with col2:
    st.markdown("### 🏪 UMKM")
    st.write("Rp 300.000")
    st.write("✔ Data penjualan\n✔ Insight bisnis\n✔ Visualisasi")

with col3:
    st.markdown("### 📊 Dashboard")
    st.write("Rp 500.000")
    st.write("✔ Power BI / Excel\n✔ Interaktif\n✔ Profesional")

st.divider()

# TESTIMONI
st.header("💬 Testimoni")

st.info("“Dashboard-nya mudah dipahami dan sangat membantu bisnis saya!”")
st.info("“Akhirnya saya ngerti data skripsi saya 🙏”")

st.divider()

# CTA AKHIR
st.header("📞 Siap Mulai?")

st.success("Klik di bawah untuk konsultasi GRATIS 🔥")

st.markdown("[👉 Hubungi via WhatsApp](https://wa.me/628xxxx)")
