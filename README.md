
## TensorFlow vs PyTorch on MNIST

This repository contains the solution for **Lab03** in the *Embedded Systems* course at **Technische Hochschule Deggendorf**, taught by **Prof. Tobias Schaffer**.

The lab focuses on implementing and comparing a simple neural network using both **TensorFlow** and **PyTorch** on the **MNIST** dataset. The trained models are also exported to embedded-friendly formats — **TensorFlow Lite** and **ONNX** — for deployment on edge devices.

---


### ✨ Objectives:
- Train the same fully-connected neural network using:
  - [x] TensorFlow (Keras API)
  - [x] PyTorch (manual loop)
- Evaluate training time, test accuracy, and model performance
- Export trained models to:
  - `.tflite` (TensorFlow Lite)
  - `.onnx` (Open Neural Network Exchange)
- Submit the implementation, exports, and a LaTeX-based lab report

---

## 🛠️ Tools & Technologies
- Python 3.11
- TensorFlow 2.x
- PyTorch 2.x
- Google Colab
- ONNX
- TensorFlow Lite
- LaTeX (Overleaf)

---

## 🧱 Model Architecture
- Input: 784 (flattened 28x28 image)
- Hidden Layer: Dense(64), ReLU activation
- Output Layer: Dense(10), logits
- Loss Function: `SparseCategoricalCrossentropy` (TF) / `CrossEntropyLoss` (PyTorch)
- Batch Size: 64
- Epochs: 5

---




