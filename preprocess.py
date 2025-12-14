from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def preprocess(df):
    le = LabelEncoder()
    df['RouteID'] = le.fit_transform(df['RouteID'])
    df['Weather'] = le.fit_transform(df['Weather'])
    X = df[['RouteID','TrafficDensity','DayOfWeek','Hour','Weather']]
    y = df['Delayed']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    scaler = StandardScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test), y_train, y_test
