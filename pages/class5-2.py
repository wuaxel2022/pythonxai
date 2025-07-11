import streamlit as st
import os

st.title("圖片元件")
st.image("image/orange-1.png", width=300)

image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=300)

image_size = st.number_input(
    "圖片大小", min_value=50, max_value=500, step=50, value=100
)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", use_container_width=True)

selected_image = st.selectbox("選擇圖片", image_files)
st.image(f"{image_folder}/{selected_image}", width=500)
