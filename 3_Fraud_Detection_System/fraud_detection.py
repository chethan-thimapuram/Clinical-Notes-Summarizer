import numpy as np
from sklearn.ensemble import IsolationForest

def demo():
    # synthetic numeric features (amount, days_since_policy, num_previous_claims)
    X = [[100, 365, 0],[1500, 12, 5],[80, 400, 0],[200000, 5, 20],[120, 200, 1]]
    X = np.array(X)
    iso = IsolationForest(contamination=0.2, random_state=42)
    iso.fit(X)
    preds = iso.predict(X)  # -1 anomaly, 1 normal
    for i,p in enumerate(preds):
        label = 'ANOMALY' if p==-1 else 'normal'
        print(f'Row {i}: {X[i].tolist()} -> {label}')

if __name__ == '__main__':
    demo()
