Email Spam Detection

A lightweight machine learning project that automatically classifies emails as spam or not spam (ham). The model is designed for high accuracy (90%+) and is ready for integration into web forms or applications.



Main Features and Objectives

Accurate spam detection: Classifies emails as spam or not spam using machine learning.



Lightweight and fast: Uses efficient algorithms suitable for real-time applications.



Text preprocessing: Includes stopword removal and TF-IDF vectorization for improved performance.



Evaluation metrics: Reports accuracy, precision, and recall.



Web integration ready: Can be deployed as a REST API for use in web forms.



How to Install and Run the Project

Download or clone this project folder to your computer.



Place your dataset (emails.csv) in the project folder. The CSV should have two columns: text (email content) and label (1 for spam, 0 for not spam).



Open a terminal or command prompt in the project folder.



Install the required Python packages with:



text

pip install pandas scikit-learn

Run the classifier script:



text

python spam\_classifier.py

Requirements

Python 3.x



pandas



scikit-learn



Example Usage / Output

After running the script, you will see output like:



text

Accuracy: 0.92

Precision: 0.91

Recall: 0.90

You can now use this model as a backend for web forms or other applications requiring spam detection.

