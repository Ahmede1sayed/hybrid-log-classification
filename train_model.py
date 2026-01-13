import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Ensure clean folder
os.makedirs("models", exist_ok=True)

# Training data
logs = [
    "API returned 404 not found error",
    "Workflow execution failed due to missing config",
    "Case escalation failed because agent is inactive",
    "Server crashed during workflow execution",
    "This module will be deprecated in version 4.0",
    "Deprecated API usage detected",
    "Module X will be retired next release",
    "System rebooted unexpectedly",
    "Multiple login failures occurred",
]

labels = [
    "Workflow Error",
    "Workflow Error",
    "Workflow Error",
    "Workflow Error",
    "Deprecation Warning",
    "Deprecation Warning",
    "Deprecation Warning",
    "Workflow Error",
    "Workflow Error",
]

# Vectorizer
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=384,   # 🔥 LOCK feature size
    stop_words="english"
)

X = vectorizer.fit_transform(logs)

# Classifier
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
model.fit(X, labels)

# Save BOTH together
joblib.dump(vectorizer, "models/tfidf_vectorizer.joblib")
joblib.dump(model, "models/log_classifier.joblib")

print("✅ Models retrained successfully")
print("Feature size:", X.shape[1])
