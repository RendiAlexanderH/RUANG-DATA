page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1551288049-bebda4e38f71");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Overlay gelap biar teks kebaca */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6); /* ini kuncinya */
    z-index: 0;
}

/* Konten di atas overlay */
.block-container {
    position: relative;
    z-index: 1;
    background: rgba(255, 255, 255, 0.9);
    padding: 2rem;
    border-radius: 15px;
}
</style>
"""
