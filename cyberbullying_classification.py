# -*- coding: utf-8 -*-
"""Cyberbullying_Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15nuFnggzKS1y0GKqKAUs3Tc3zG4iKm0u
"""

import pandas as pd

# Load the dataset from the provided Excel file
file_path = '/content/DATASET CYBERBULLYING TWITTER.xlsx'
dataset = pd.read_excel(file_path)

# Display the first few rows of the dataset to understand its structure
dataset.head()

# Using NLTK's stopwords for Indonesian (but stemming will be skipped)
import nltk
nltk.download('stopwords')

import re

# List of provided Indonesian stopwords
indonesian_stopwords_custom = [
    'yang', 'dan', 'di', 'ke', 'dari', 'untuk', 'dengan', 'akan', 'pada', 'sebagai',
    'adalah', 'itu', 'ini', 'karena', 'oleh', 'atau', 'jika', 'dalam', 'sudah', 'tidak',
    'sangat', 'lebih', 'dari', 'kita', 'mereka', 'kamu', 'saya', 'dia', 'kami', 'anda',
    'bukan', 'hanya', 'bisa', 'masih', 'lagi', 'harus', 'setelah', 'sebelum', 'agar',
    'begitu', 'supaya', 'walaupun', 'tetapi', 'namun', 'maka'
]

# Update the cleaning function to use the custom stopwords list
def clean_text_custom_stopwords(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove URLs, mentions, hashtags, punctuation, and numbers
    text = re.sub(r"http\S+|www\S+|@\w+|#\w+|[^\w\s]|[\d]", "", text)

    # Remove stopwords
    text_tokens = text.split()
    filtered_text = [word for word in text_tokens if word not in indonesian_stopwords_custom]

    return ' '.join(filtered_text)

# Apply the updated cleaning function to the 'Komentar' column
dataset['Cleaned_Comments'] = dataset['Komentar'].apply(clean_text_custom_stopwords)

# Display the cleaned dataset
dataset[['Komentar', 'Cleaned_Comments', 'Kategori']].head()

"""## TF-IDF Vectorization:"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Define the TF-IDF vectorizer with unigram and bigram range
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)

# Fit and transform the cleaned comments
X = tfidf_vectorizer.fit_transform(dataset['Cleaned_Comments'])

# Define the target variable (labels)
y = dataset['Kategori']

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training data shape: {X_train.shape}")
print(f"Test data shape: {X_test.shape}")

"""## Machine Learning Algorithms:

### Logistic Regression:
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Initialize and train the Logistic Regression model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

# Predict and evaluate
y_pred_logreg = logreg.predict(X_test)
print("Logistic Regression Classification Report:\n", classification_report(y_test, y_pred_logreg))

from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support

def get_metrics(y_true, y_pred):
    # Get precision, recall, f1-score and support
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    accuracy = accuracy_score(y_true, y_pred)
    return accuracy, precision, recall, f1

# Logistic Regression
accuracy_logreg, precision_logreg, recall_logreg, f1_logreg = get_metrics(y_test, y_pred_logreg)
print(f"Logistic Regression - Accuracy: {accuracy_logreg}, Precision: {precision_logreg}, Recall: {recall_logreg}, F1-Score: {f1_logreg}")

"""### Support Vector Machines (SVM):"""

from sklearn.svm import SVC

# Initialize and train the SVM model
svm_model = SVC(kernel='linear', probability=True)
svm_model.fit(X_train, y_train)

# Predict and evaluate
y_pred_svm = svm_model.predict(X_test)
print("SVM Classification Report:\n", classification_report(y_test, y_pred_svm))

from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support

def get_metrics(y_true, y_pred):
    # Get precision, recall, f1-score and support
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    accuracy = accuracy_score(y_true, y_pred)
    return accuracy, precision, recall, f1

# SVM
accuracy_svm, precision_svm, recall_svm, f1_svm = get_metrics(y_test, y_pred_svm)
print(f"Support Vector Machine - Accuracy: {accuracy_svm}, Precision: {precision_svm}, Recall: {recall_svm}, F1-Score: {f1_svm}")

"""### Random Forest Classifier:"""

from sklearn.ensemble import RandomForestClassifier

# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Predict and evaluate
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Classification Report:\n", classification_report(y_test, y_pred_rf))

from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support

def get_metrics(y_true, y_pred):
    # Get precision, recall, f1-score and support
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    accuracy = accuracy_score(y_true, y_pred)
    return accuracy, precision, recall, f1

# Random Forest
accuracy_rf, precision_rf, recall_rf, f1_rf = get_metrics(y_test, y_pred_rf)
print(f"Support Vector Machine - Accuracy: {accuracy_rf}, Precision: {precision_rf}, Recall: {recall_rf}, F1-Score: {f1_rf}")

"""### Naive Bayes (MultinomialNB):"""

from sklearn.naive_bayes import MultinomialNB

# Initialize and train the Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# Predict and evaluate
y_pred_nb = nb_model.predict(X_test)
print("Naive Bayes Classification Report:\n", classification_report(y_test, y_pred_nb))

from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support

def get_metrics(y_true, y_pred):
    # Get precision, recall, f1-score and support
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    accuracy = accuracy_score(y_true, y_pred)
    return accuracy, precision, recall, f1

# Naive Baiyes
accuracy_nb, precision_nb, recall_nb, f1_nb = get_metrics(y_test, y_pred_nb)
print(f"Support Vector Machine - Accuracy: {accuracy_nb}, Precision: {precision_nb}, Recall: {recall_nb}, F1-Score: {f1_nb}")

"""## Evaluation Metrics:"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming the metrics have already been calculated as shown in the previous code
# Create a DataFrame with all metrics
model_metrics = pd.DataFrame({
    'Model': ['Logistic Regression', 'SVM', 'Random Forest', 'Naive Bayes'],
    'F1-Score': [f1_logreg, f1_svm, f1_rf, f1_nb],
    'Recall': [recall_logreg, recall_svm, recall_rf, recall_nb],
    'Accuracy': [accuracy_logreg, accuracy_svm, accuracy_rf, accuracy_nb],
})

# Sort by F1-Score
sorted_model_metrics = model_metrics.sort_values(by='F1-Score', ascending=False)

# Melt the DataFrame for seaborn
melted_metrics = pd.melt(sorted_model_metrics, id_vars=['Model'], var_name='Metrics', value_name='Score')

# Plotting
plt.figure(figsize=(10, 6))
sns.set(style="darkgrid")

sns.lineplot(data=melted_metrics, x='Metrics', y='Score', hue='Model', marker='o')

plt.title('Model Performance Metrics')
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.legend(title='Model', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Function to plot confusion matrix
def plot_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Non-bullying', 'Bullying'], yticklabels=['Non-bullying', 'Bullying'])
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

# Predictions for each model (assuming they are already calculated as per your code)
y_pred_logreg = logreg.predict(X_test)
y_pred_svm = svm_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)
y_pred_nb = nb_model.predict(X_test)

# Plotting confusion matrices
plot_confusion_matrix(y_test, y_pred_logreg, "Logistic Regression")
plot_confusion_matrix(y_test, y_pred_svm, "Support Vector Machine (SVM)")
plot_confusion_matrix(y_test, y_pred_rf, "Random Forest")
plot_confusion_matrix(y_test, y_pred_nb, "Naive Bayes")