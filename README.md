# Urdu OCR – Fine-Tuned TrOCR Model for Urdu Text Recognition

> A deep learning-based Optical Character Recognition (OCR) project developed during the **Code Saviours (SMC-PRIVATE) Limited ML/AI Internship Programme – Batch SI-26**.

---

# 📌 Project Overview

Urdu Optical Character Recognition (OCR) is a challenging computer vision task due to the cursive nature of the Urdu script, multiple writing styles, ligatures, varying fonts, and complex character connections.

This project focuses on building an Urdu OCR system using Microsoft's **TrOCR (Transformer-based Optical Character Recognition)** model. The model was fine-tuned on a custom Urdu image dataset collected during the internship.

The final application provides a simple interface where users can upload an Urdu text image and receive the extracted text.

---

# 🎯 Problem Statement

Extracting Urdu text from images is considerably more difficult than English OCR because:

- Urdu characters are connected.
- Characters change shape depending on their position.
- Different fonts produce different character appearances.
- Images may contain noise, blur, or complex backgrounds.

This project aims to automate Urdu text extraction using deep learning.

---

# 🌍 Why This Project Matters

Accurate Urdu OCR has many real-world applications:

- Digitizing Urdu books
- Newspaper archiving
- Historical document preservation
- Educational resources
- Government document digitization
- Searchable Urdu documents

---

# 🚀 Features

- Fine-tuned TrOCR model
- Urdu handwritten/printed text recognition
- Image upload interface
- Automatic text extraction
- Simple Gradio web interface
- Hugging Face deployment support

---

# 📅 Internship Workflow (Week 1 → Week 5)

## ✅ Week 1 – Dataset Collection

Collected and organized Urdu text images.

Tasks completed:

- Downloaded Urdu OCR dataset
- Selected sample images
- Organized dataset folders
- Uploaded dataset to GitHub
- Prepared images for training

---

## ✅ Week 2 – Data Preparation

Prepared dataset for model training.

Tasks completed:

- Cleaned dataset
- Matched images with labels
- Organized training files
- Generated training samples
- Prepared model input format

---

## ✅ Week 3 – Model Fine-Tuning

Fine-tuned Microsoft's TrOCR model.

Main steps:

- Loaded pretrained TrOCR model
- Loaded processor
- Created custom dataset
- Tokenized labels
- Trained using Hugging Face Transformers
- Saved trained model

Technologies:

- Python
- PyTorch
- Transformers
- Google Colab

---

## ✅ Week 4 – Model Evaluation

Evaluated the trained model.

Activities:

- Loaded trained model
- Generated predictions
- Compared predictions with ground truth
- Calculated evaluation metrics

### Results

The model was successfully trained and tested.

However, prediction accuracy remained low due to:

- Small fine-tuning dataset
- Limited number of annotated samples
- Limited training epochs
- Dataset diversity

With a larger annotated dataset and additional training, performance is expected to improve significantly.

---

## ✅ Week 5 – Deployment

Created an OCR web application using Gradio.

Deployment workflow:

- Load trained model
- Upload Urdu image
- Generate prediction
- Display extracted Urdu text

Deployment target:

- Hugging Face Spaces
- Gradio Interface

---

# 🧠 Model Used

**Model:** Microsoft TrOCR

Base Model:

```
microsoft/trocr-base-printed
```

Framework:

- Hugging Face Transformers

Architecture:

- Vision Encoder Decoder

---

# 📂 Dataset Details

Dataset Type:

Urdu OCR Dataset

Contents:

- Urdu text images
- Multiple fonts
- Different text styles
- Various image sizes

Training Samples:

Custom annotated Urdu images prepared during the internship.

---

# ⚙️ Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- TrOCR
- Google Colab
- Gradio
- Git
- GitHub
- Hugging Face Spaces
- Pillow

---

# 📁 Project Structure

```
Urdu-OCR/
│
├── app.py
├── requirements.txt
├── README.md
├── model/
├── dataset/
├── images/
├── notebooks/
└── outputs/
```

---

# 🌐 Live Demo

## Hugging Face Space

> **Paste your Hugging Face Space URL here**

Example:

```
https://huggingface.co/spaces/yourusername/urdu-ocr-codesaviours-si26-saima
```

---

# 💻 How to Run Locally

## Clone Repository

```bash
git clone https://github.com/yourusername/your-repository.git
```

---

## Move into Project

```bash
cd your-repository
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

or

```bash
python3 app.py
```

The Gradio application will open in your browser.

---

# 📦 Requirements

```
transformers==4.35.0
torch==2.0.1
gradio==3.50.0
Pillow==10.0.0
```

---

# 📸 Application Workflow

1. Upload an Urdu text image.
2. The image is processed using the TrOCR processor.
3. The trained model predicts the text.
4. The extracted Urdu text is displayed.

---

# 📊 Results

The project demonstrates the complete workflow of developing an OCR system:

- Dataset preparation
- Data preprocessing
- Model fine-tuning
- Evaluation
- Web interface development
- Deployment

Although the final prediction accuracy remained limited due to the small training dataset, the project successfully demonstrates the end-to-end implementation of an Urdu OCR pipeline.

---

# ⚠️ Limitations

Current limitations include:

- Small fine-tuning dataset
- Limited annotated images
- Limited training epochs
- Performance decreases on unseen fonts
- Sensitive to noisy images

---

# 🔮 Future Improvements

Future work may include:

- Increase dataset size
- Add handwritten Urdu samples
- Train for more epochs
- Hyperparameter tuning
- Data augmentation
- Improve inference accuracy
- Deploy a production-ready OCR service

---

# 🙏 Acknowledgements

Special thanks to:

- Code Saviours (SMC-PRIVATE) Limited
- ML/AI Internship Programme – Batch SI-26
- Hugging Face
- Microsoft Research
- PyTorch
- Google Colab

---

# 👩‍💻 Author

**Saima Manzoor**

BS Computer Science

The University of Faisalabad

---

# 🎓 Internship Credit

Built during the **Code Saviours (SMC-PRIVATE) Limited ML/AI Internship Programme – Batch SI-26**.

---

# 📜 License

This project is developed for educational and research purposes during the Code Saviours ML/AI Internship Programme.
