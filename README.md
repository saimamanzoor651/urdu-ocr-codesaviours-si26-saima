# Urdu OCR Project | Code Saviours SI-26 | Saima Manzoor

## Week 1 - Project Setup

This repository contains my work for Week 1 of the Code Saviours ML/AI Internship.

### Objectives
- Set up GitHub, Google Colab, and Hugging Face
- Learn the basics of Urdu OCR
- Collect and organize 100+ Urdu text images
- Create a labels.csv file for OCR training

## Repository Structure

```text
data/
└── raw/
    ├── books/
    ├── newspaper/
    ├── other/
    ├── signboards/
    └── synthetic/

README.md
SI26_Week1_Saima.ipynb
labels.csv
```
## Why We Need a Better Model

Tesseract fails on Urdu because Urdu is a cursive script with connected letters, changing character shapes, and complex ligatures. It struggles with different fonts, image quality, and connected handwriting, resulting in incorrect or incomplete text recognition. Therefore, a dedicated Urdu OCR model is needed for better accuracy.
