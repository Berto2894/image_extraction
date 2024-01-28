import streamlit as st
from PIL import Image
import pytesseract

# Path ke binary Tesseract (contoh di Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\uSeR\AppData\Local\Programs\Tesseract-OCR'

def extract_text_from_image(image):
    # Ekstraksi teks menggunakan Tesseract OCR
    text = pytesseract.image_to_string(image)
    return text

def main():
    st.title("Ekstraksi Teks dari Gambar")

    # File Uploader untuk mengunggah gambar
    uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Tampilkan gambar yang diunggah
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang Diunggah", use_column_width=True)

        # Tombol untuk ekstraksi teks
        if st.button("Ekstrak Teks"):
            # Ekstraksi teks dari gambar
            extracted_text = extract_text_from_image(image)
            
            # Tampilkan hasil ekstraksi
            st.subheader("Hasil Ekstraksi Teks:")
            st.text(extracted_text)

if __name__ == "__main__":
    main()
