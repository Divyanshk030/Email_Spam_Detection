import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Step 1: Load your data
data = pd.read_csv('emails.csv')

# Step 2: Preprocess the text (make it lowercase)
data['text'] = data['text'].str.lower()

# Step 3: Convert text to numbers (vectorization)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 6: Test the model
y_pred = model.predict(X_test)

# Step 7: Show results
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
