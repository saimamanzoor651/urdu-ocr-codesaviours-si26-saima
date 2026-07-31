<div align="center">

# 📝 Urdu OCR using TrOCR

### Fine-Tuning a Transformer-Based OCR Model for Urdu Text Recognition

**Code Saviours (SMC-PRIVATE) Limited**  
**ML / AI Internship Programme – Batch SI-26**

**Developed by:** **Saima Manzoor**

</div>

---

# 📖 About the Project

Optical Character Recognition (OCR) is a computer vision technology that converts text from images into machine-readable text. While OCR performs well for many languages, Urdu remains a challenging language because of its cursive writing style, connected characters, and different font variations.

This project was completed as part of the **Code Saviours ML/AI Internship (Batch SI-26)**. Throughout the internship, I learned the complete workflow of developing an OCR system, including dataset preparation, preprocessing, model fine-tuning, evaluation, and building a simple user interface for text extraction.

The project uses **Microsoft's TrOCR (Transformer-based Optical Character Recognition)** model as the foundation for recognizing Urdu text from images.

---

# 🎯 Project Objectives

The main objective of this project was to:

- Learn the complete OCR development workflow.
- Understand transformer-based OCR models.
- Fine-tune a pretrained TrOCR model on an Urdu dataset.
- Build a simple interface for extracting Urdu text from images.
- Organize the complete project on GitHub following professional development practices.

---

# 🌍 Why Urdu OCR?

Urdu OCR can be useful in many practical applications, including:

- 📚 Digitizing books and newspapers
- 🎓 Educational resources
- 🏛 Historical document preservation
- 📄 Government record digitization
- 🔍 Searchable Urdu archives

---

# 🚀 Internship Progress

## ✅ Week 1 – Introduction & Dataset Preparation

The first week focused on understanding Optical Character Recognition (OCR), exploring the project requirements, and preparing the dataset for future training.

### Tasks Completed

- Learned the basics of OCR.
- Understood the internship project requirements.
- Created the GitHub repository.
- Created a Hugging Face account as part of the initial project setup.
- Collected and organized Urdu OCR images.
- Prepared the project workspace.

---

## ✅ Week 2 – Dataset Organization

During this stage, the dataset was prepared for model training.

### Tasks Completed

- Organized image files.
- Prepared labels for training.
- Structured the dataset for machine learning.
- Verified data before training.

---

## ✅ Week 3 – Dataset Expansion & Data Loading

The dataset was expanded to include more than **200 Urdu images** to improve the training process. A custom dataset loader was also prepared for efficient data loading.

### Tasks Completed

- Expanded the dataset.
- Prepared the training dataset.
- Built the custom data loader.
- Loaded images and labels into the training pipeline.

---

## ✅ Week 4 – Model Fine-Tuning

This week focused on fine-tuning the pretrained **Microsoft TrOCR** model.

### Training Workflow

- Loaded the pretrained TrOCR model.
- Loaded the TrOCR processor.
- Prepared the Urdu dataset.
- Split the dataset for training and evaluation.
- Fine-tuned the model.
- Saved the trained model.

### Base Model

```text
microsoft/trocr-base-printed
```

### Evaluation

The trained model was evaluated using the prepared dataset to understand its prediction performance.

Although the complete OCR pipeline was successfully implemented, the current model still has room for improvement due to the limited training dataset and available training time.

---

## ✅ Week 5 – OCR Interface Development

In the final week, a simple OCR interface was created using **Gradio**.

The interface allows users to:

- Upload an Urdu text image.
- Process the image using the trained model.
- Display the extracted Urdu text.

This completed the end-to-end workflow from data preparation to user interaction.

---

# 🧠 Model Information

| Item | Details |
|------|---------|
| **Base Model** | `microsoft/trocr-base-printed` |
| **Architecture** | Vision Encoder Decoder (TrOCR) |
| **Framework** | Hugging Face Transformers |
| **Deep Learning Library** | PyTorch |

---

# 📂 Dataset Details

The dataset contains Urdu text images collected and organized during the internship.

### Dataset Characteristics

- Printed Urdu text
- Multiple font styles
- Different image sizes
- Custom processed images

The processed images are available inside the **data/processed** directory.

---

# 🛠 Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- Microsoft TrOCR
- Google Colab
- Gradio
- Pillow
- Git
- GitHub

---

# ⚙️ How the System Works

1. Upload an Urdu image.
2. The image is processed using the TrOCR processor.
3. The trained model predicts the text.
4. The extracted Urdu text is displayed.

---

# 📁 Project Structure

```text
urdu-ocr-codesaviours-si26-saima/
│
├── data/
│   └── processed/
│
├── SI26_Week1_Saima.ipynb
├── si26_week2_saima.ipynb
├── SI26_Week3_Saima.ipynb
├── SI26_Week4_Saima.ipynb
├── SI26_Week5_Saima.ipynb
│
├── app.py
├── labels.csv
├── requirements.txt
└── README.md
```

---

# 💻 Running the Project

### Clone the Repository

```bash
git clone https://github.com/saimamanzoor651/urdu-ocr-codesaviours-si26-saima.git
```

### Move to the Project Folder

```bash
cd urdu-ocr-codesaviours-si26-saima
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

---

# 📦 Required Libraries

```text
transformers==4.35.0
torch==2.0.1
gradio==3.50.0
Pillow==10.0.0
```

---

# 📊 Results

This project demonstrates the complete workflow of building an Urdu OCR system using transformer-based deep learning techniques.

The project successfully covers:

- Dataset preparation
- Data organization
- Dataset expansion
- Model fine-tuning
- Model evaluation
- OCR interface development

The implementation provided valuable practical experience in computer vision, OCR, and transformer-based deep learning.

---

# ⚠️ Challenges

Some challenges faced during the project include:

- Limited annotated training data
- Urdu character complexity
- Performance on unseen images
- Limited computational resources

---

# 🔮 Future Improvements

Future improvements may include:

- Increasing the dataset size
- Including handwritten Urdu text
- Applying data augmentation
- Training for additional epochs
- Improving prediction accuracy
- Deploying the application on a production-ready platform

---

# 🙏 Acknowledgements

I would like to thank:

- Code Saviours (SMC-PRIVATE) Limited
- ML / AI Internship Programme – Batch SI-26
- Microsoft for providing the pretrained TrOCR model
- Hugging Face Transformers
- PyTorch
- Google Colab

---

# 👩‍💻 Author

**Saima Manzoor**

BS Computer Science

The University of Faisalabad

**GitHub:** https://github.com/saimamanzoor651

---

# 📜 Internship Credit

**Built during the Code Saviours (SMC-PRIVATE) Limited ML / AI Internship Programme – Batch SI-26.**
