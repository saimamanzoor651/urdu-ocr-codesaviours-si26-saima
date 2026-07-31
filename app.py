
import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

st.set_page_config(page_title="Urdu OCR", page_icon="📖")

MODEL_PATH = "/content/drive/MyDrive/SI26-urdu-ocr-model"

@st.cache_resource
def load_model():
    processor = TrOCRProcessor.from_pretrained(MODEL_PATH, use_fast=False)
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_PATH)
    model.eval()
    return processor, model

processor, model = load_model()

st.title("Urdu OCR - Code Saviours SI-26")
st.write("Upload an Urdu text image and extract the text.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    pixel_values = processor(
        image,
        return_tensors="pt"
    ).pixel_values

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)

    text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    st.subheader("Extracted Text")

    if text.strip() == "":
        st.warning("Could not extract text.")
    else:
        st.success(text)
