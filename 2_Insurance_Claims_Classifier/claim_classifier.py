import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def demo():
    # small synthetic demo dataset
    data = pd.DataFrame({
        'claim_text':[
            'Patient fell from ladder and broke arm',
            'Car accident with whiplash injury',
            'Dental cleaning and cavity filling',
            'House fire damage to roof and walls',
            'Medication refill for chronic condition'
        ],
        'category':['injury','injury','dental','property','medication']
    })
    X = data['claim_text']
    y = data['category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    vec = TfidfVectorizer(max_features=1000)
    X_train_t = vec.fit_transform(X_train)
    X_test_t = vec.transform(X_test)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train_t, y_train)
    pred = clf.predict(X_test_t)
    print('Classification report:\n', classification_report(y_test, pred))

if __name__ == '__main__':
    demo()
