import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io
st.title("My Image Editing Studio")
st.write("Welcome to my first python project")
uploaded_image = st.file_uploader("choose an image", type=["jpg", "jpeg", "png"])
#if uploaded_image is not None:
    #st.image(uploaded_image, caption="Your Original Image")
if uploaded_image is not None:   
    original_image = Image.open(uploaded_image)
    st.image(original_image, caption="Your Original Image")
    st.subheader("Adjust Brightness")
    brightness=st.slider("Brightness", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
    enhancer=ImageEnhance.Brightness(original_image)
    bright_image=enhancer.enhance(brightness)
    st.image(bright_image,caption="Brightness preview")
    st.subheader("Adjust contrast")
    contrast=st.slider("contrast", min_value=0.5, max_value=2.0, value=0.1, step=0.1)
    contrast_enhancer=ImageEnhance.Contrast(bright_image)
    contrast_image=contrast_enhancer.enhance(contrast)
    st.image(contrast_image, caption="Contrast Preview")
    image_bytes = io.BytesIO()
    contrast_image.save(image_bytes, format="PNG")
    st.download_button(label="Download Edited Image",
                       data=image_bytes.getvalue(),
                       file_name="edited image.png", mime="image/png")
    if st.button("convert to Black and White"):
        gray_image=ImageOps.grayscale(original_image)
        st.image(gray_image, caption="Black and Whaite")
        st.success("Image converted successfully")
