app_code = """
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
from PIL import Image

st.title("Minimal Digit Classifier Test")

st.write("Draw a digit below and click Classify (dummy classifier).")

canvas_result = st_canvas(
    stroke_width=10,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA').convert('L')
    st.image(img, caption="Your drawing (grayscale)")

    if st.button("Classify"):
        st.write("Pretend we classified this as digit: **7**")
"""

with open("app.py", "w") as f:
    f.write(app_code)
