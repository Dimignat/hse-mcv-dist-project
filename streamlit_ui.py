"""
Streamlit UI
"""
import cv2
import numpy as np
import streamlit as st

from test_project.demo import process_image


current_img = cv2.imread("test_project/gosling.jpeg")
current_img = cv2.cvtColor(current_img, cv2.COLOR_BGR2RGB)

st.header("Demo")

uploaded_file = st.file_uploader(label="Select current image")
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    imageBGR = cv2.imdecode(file_bytes, 1)
    current_img = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)

st.image(current_img, caption="Current image")

if st.button("Process image", use_container_width=True):
    out1, out2, out3 = process_image(current_img, show=False)
    st.image(out1, caption="Output 1")
    st.image(out2, caption="Output 2")
    st.image(out3, caption="Output 3")
