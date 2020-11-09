# Load modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler as ss
from sklearn.svm import SVC

# Load dataset
df = pd.read_csv(r"dataset.csv",header=None)

df.columns=['Age','Sex','Chest_Pain','Rest_BP','Cholestrol','Fast_BS','Rest_ECG','Max_Heart_Rate','Exercise','ExertoRest','Slope','No_Major_Vessels','Thal','Heart_Disease']
df['Heart_Disease'] = df.Heart_Disease.map({0: 0, 1: 1, 2: 1, 3: 1, 4: 1})
# Split into training data and test data
# X = df[['Age','Sex','Chestpain','RestBP','Chol','Fast BS','RestECG','MaxHRate','Exercise','ExertoRest','Slope','No_Major_Vessels','Thal']]
# y = df['Heart_Disease']

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
sc = ss()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Now we’ll fit the model on the training data




classifier = SVC(kernel = 'rbf')
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)




# Pickle model
pd.to_pickle(classifier,r'svc.pickle')

# Unpickle model
model_SVM = pd.read_pickle(r'svc.pickle')

# Take input from user

Age= int(input("Enter Patient Age"))
Sex=int(input("Enter Patient Sex"))
Chest_Pain=int(input("Enter Chest Pain: "))
Rest_BP = int(input("Enter Rest BP: "))
Cholestrol= int(input("Enter Cholestrol: "))
Fast_BS=int(input("Enter Fast Blood Sugar: "))
Rest_ECG= int(input("Enter ECG: "))
Max_Heart_Rate=int(input("Enter Max Heart Rate: "))
Exercise=int(input("Enter Excercise: "))
ExertoRest=float(input("Enter ExertoRest: "))
Slope=int(input("Enter Slope: "))
No_Major_Vessels=int(input("Enter No of major vessels: "))
Thal=int(input("Enter Thal: "))
result = model_SVM.predict([[Age, Sex,Chest_Pain, Rest_BP, Cholestrol,Fast_BS,Rest_ECG,Max_Heart_Rate,Exercise,ExertoRest,Slope,No_Major_Vessels,Thal]])  # input must be 2D array
print(result)