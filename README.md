# Urdu Handwritten OCR

A machine learning project that uses a fine-tuned TrOCR model to recognize Urdu text from uploaded images.

## Why This Matters

Urdu text is difficult for traditional OCR systems because Urdu has connected characters, different writing styles, and a right-to-left script. This project aims to make Urdu text recognition easier by allowing users to upload an image and receive a predicted text output. Such systems can help with digitizing documents, books, handwritten content, and historical records.

## Live Demo

Try the project here:

https://huggingface.co/spaces/Saima-Manzoor/urdu-ocr-demo

<img width="1916" height="736" alt="image" src="https://github.com/user-attachments/assets/edcb6850-d8ef-411c-8582-5b73f1bd781f" />


## How It Works

The project uses images containing Urdu text along with their corresponding labels. The images are processed and used to fine-tune Microsoft's TrOCR model. During prediction, a user uploads an image through the web interface, and the trained model generates the predicted text. The result is then displayed directly to the user.

## Results

The model was trained for **3 epochs** using a dataset of **203 Urdu text images**.

- Training samples: **162**
- Testing samples: **41**
- Final Training Loss: **3.5003**
- Average Test Loss: **3.5345**
- Character-Level Accuracy: **0.00%**

The current accuracy shows that the complete OCR pipeline was successfully implemented, but the model requires further improvement. A larger dataset, more training epochs, and better Urdu-specific training data could improve the prediction performance.

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- Microsoft TrOCR
- Gradio
- Hugging Face Spaces
- Pillow

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/saimamanzoor651/urdu-ocr-codesaviours-si26-saima.git
````

Move into the project folder:

```bash
cd urdu-ocr-codesaviours-si26-saima
```

Install the required packages:

```bash
pip install gradio torch torchvision transformers spaces Pillow
```

Run the application:

```bash
python app.py
```

After starting the application, open the local URL shown in the terminal and upload an Urdu text image to test the OCR model.

## Project Structure

```text
urdu-ocr-codesaviours-si26-saima/
│
├── data/
│   └── processed/raw
│
├── SI26_Week1_Saima.ipynb
├── SI26_Week3_Saima.ipynb
├── SI26_Week4_Saima.ipynb
├── SI26_Week5_Saima.ipynb
│
├── app.py
├── requirements.txt
├── labels.csv
└── README.md
```

## Future Improvements

* Train on a larger Urdu OCR dataset.
* Increase the number of training epochs.
* Improve image preprocessing.
* Use more diverse handwriting and font styles.
* Improve character-level accuracy.
* Further optimize the Hugging Face demo.

---

**Built by: Saima Manzoor | Code Saviours SI-26 | 2026**
