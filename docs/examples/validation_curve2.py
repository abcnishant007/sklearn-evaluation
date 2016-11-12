import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.learning_curve import validation_curve

from sklearn_evaluation import plot

param_range = np.array([1, 10, 100])
param_name = "n_estimators"
train_scores, test_scores = validation_curve(
    RandomForestClassifier(), X, y,
    param_name=param_name,
    param_range=param_range,
    cv=10, scoring="accuracy", n_jobs=1)

plot.validation_curve(train_scores, test_scores, param_range, param_name,
                      semilogx=False)
plt.show()
