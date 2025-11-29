# filename: heatmap_app.py

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Image Heatmap Generator")

st.title("Image to Heatmap Converter")
st.write("Upload an image and see its heatmap representation!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    img = Image.open(uploaded_file).convert('L')  # convert to grayscale

    # Resize to make smaller matrix
    img = img.resize((50, 50))
    data = np.array(img)

    # Display the original image
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Create heatmap
    fig, ax = plt.subplots()
    cax = ax.imshow(data, cmap='hot')
    fig.colorbar(cax)

    # Display heatmap
    st.pyplot(fig)
