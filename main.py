import streamlit as st

# CONFIG
st.set_page_config(
    page_title="Ruang Data",
    layout="wide"
)

# STYLE (AMAN, TIDAK BIKIN BLANK)
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stButton>button {
    background-color: #22c55e;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HERO SECTION
# ======================
st.title("📊 Ruang Data")
st.subheader("Pahami Data Tanpa Ribet")

st.write("""
Kami membantu mahasiswa dan UMKM memahami,
mengolah, dan menganalisis data secara praktis.
""")

st.success("🚀 Ubah data jadi keputusan yang tepat!")

if st.button("📞 Konsultasi Sekarang"):
    st.markdown("👉 Hubungi WhatsApp: https://wa.me/628xxxx")

st.divider()

# ======================
# LAYANAN
# ======================
st.header("💼 Layanan Kami")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ✔ Konsultasi Data  
    ✔ Analisis & Visualisasi  
    """)

with col2:
    st.markdown("""
    ✔ Dashboard (Excel / Power BI)  
    ✔ Insight & Rekomendasi  
    """)

st.divider()

# ======================
# PAKET HARGA
# ======================
st.header("💰 Paket Harga")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎓 Mahasiswa")
    st.write("Rp 150.000")
    st.caption("Skripsi, tugas, analisis dasar")

with col2:
    st.subheader("🏪 UMKM")
    st.write("Rp 300.000")
    st.caption("Analisis penjualan & insight bisnis")

with col3:
    st.subheader("📊 Dashboard")
    st.write("Rp 500.000")
    st.caption("Dashboard Power BI / Excel")

st.divider()

# ======================
# TESTIMONI
# ======================
st.header("💬 Testimoni")

st.info("“Sangat membantu! Data jadi mudah dipahami.”")
st.info("“Dashboard-nya simpel dan langsung bisa dipakai.”")

st.divider()

# ======================
# KONTAK
# ======================
st.header("📞 Kontak")

st.write("📧 Email: ruangdata@email.com")
st.write("📱 WhatsApp: 08xxxxxxxxxx")
st.write("📷 Instagram: @ruangdata")

st.success("🔥 Siap bantu kamu memahami data dengan mudah!")
