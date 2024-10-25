import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Sample Data
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [20, 25, 30, None, 40],
    'Gender': ['Male', 'Female', 'Female', 'Male', None],
    'AnnualIncome': [15, 18, 22, 30, None],
    'SpendingScore': [39, 81, None, 77, 56]
}
df = pd.DataFrame(data)

# Preprocessing Steps
# 1. Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['AnnualIncome'].fillna(df['AnnualIncome'].median(), inplace=True)
df['SpendingScore'].fillna(df['SpendingScore'].mean(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

# 2. Encode categorical variables
df = pd.get_dummies(df, columns=['Gender'], drop_first=True)

# 3. Scale numerical features
scaler = MinMaxScaler()
df[['Age', 'AnnualIncome', 'SpendingScore']] = scaler.fit_transform(df[['Age', 'AnnualIncome', 'SpendingScore']])

# 4. Split the data
X = df.drop(columns=['CustomerID', 'SpendingScore'])
y = df['SpendingScore']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Output results
print("Training Features:\n", X_train)
print("Testing Features:\n", X_test)
print("Training Labels:\n", y_train)
print("Testing Labels:\n", y_test)
