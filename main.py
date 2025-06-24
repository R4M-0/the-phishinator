from src.utils import load_dataset
from src.feature_engineering import extract_features
from src.model import train_model, evaluate_model
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import joblib

def tune_model(X_train, y_train):
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }

    grid = GridSearchCV(
        RandomForestClassifier(random_state=42),
        param_grid,
        cv=3,
        scoring='f1_macro',  # balance of precision and recall
        n_jobs=-1
    )

    grid.fit(X_train, y_train)
    print("Best parameters:", grid.best_params_)
    joblib.dump(grid.best_estimator_, 'api/models/phishing_model.pkl')
    return grid.best_estimator_


def main():
    print("Loading dataset...")
    df = load_dataset('data/new_data_urls.csv')

    print("Extracting features...")
    X = df['url'].apply(lambda u: pd.Series(extract_features(u)))
    y = df['status']  # 0=phishing, 1=legit

    print(f"Dataset shape: {df.shape}")
    print("Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("Training model...")
    model = tune_model(X_train, y_train)

    print("Evaluating model...")
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
