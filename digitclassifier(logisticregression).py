# -*- coding: utf-8 -*-
"""digitclassifier(logisticregression).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1INwTz_OXfsS3dL6oA3Wgou2-rRi1Q1YR
"""

# Import necessary libraries
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# Load MNIST dataset
print("Loading MNIST dataset...")
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist["data"], mnist["target"]

# Convert labels to integers
y = y.astype(np.uint8)

# Normalize pixel values to 0–1 range
X = X / 255.0

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize Logistic Regression model
print("Training Logistic Regression model...")
log_reg = LogisticRegression(solver='lbfgs', max_iter=1000, multi_class='auto')
log_reg.fit(X_train, y_train)

# Make predictions
print("Evaluating model...")
y_pred = log_reg.predict(X_test)

# Performance metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))