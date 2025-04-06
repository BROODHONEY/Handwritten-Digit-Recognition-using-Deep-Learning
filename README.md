# 🧠 Handwritten Digit Recognizer with CNN (MNIST)

This project is a basic Convolutional Neural Network (CNN) built using **TensorFlow** and **Keras** to classify handwritten digits from the **MNIST** dataset. The model learns to identify digits (0–9) from grayscale images and achieves high accuracy with minimal training.

---

## 🔍 Project Overview

- **Dataset**: [MNIST Handwritten Digits](http://yann.lecun.com/exdb/mnist/)
- **Model Type**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras
- **Goal**: Classify 28x28 grayscale images into one of 10 digit classes.

---

## 📦 Dependencies

Make sure you have the following Python libraries installed:

```bash
pip install tensorflow keras matplotlib numpy pandas pillow
```
-  Python 3.9–3.12

---

## 📁 Project Structure

```bash
.
├── Training.py                # Model training script
├── canvas_image.ps            # Canvas postscript 
├── GUI.py                     # GUI script
├── DigitRecognizer.py         # Main script
├── digit_recognizer_model.h5  # Saved trained model
└── README.md                  # Project documentation
```
---

## 🚀 How to Run

1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/digit-recognizer-cnn.git
  cd digit-recognizer-cnn
  ```
2. Create a virtual environment:
  ```bash
  python3 -m venv .venv
  ```
3. Run the Main Script:
  ```bash
  python DigitRecognizer.py
  ```
---

## 📈 Training & Evaluation

- Epochs: 5
- Batch Size: 128
- Optimizer: AdamLoss Function: Categorical Crossentropy
- Accuracy Achieved: ~98% on test set
After training, evaluation metrics like test loss and test accuracy are printed.
