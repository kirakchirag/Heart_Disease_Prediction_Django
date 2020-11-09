# Load modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



df = pd.read_csv(r"dataset.csv",header=None)

df.columns=['Age','Sex','Chest_Pain','Rest_BP','Cholestrol','Fast_BS','Rest_ECG','Max_Heart_Rate','Exercise','ExertoRest','Slope','No_Major_Vessels','Thal','Heart_Disease']



X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values



# Create training and testing vars, It’s usually around 80/20 or 70/30.
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Now we’ll fit the model on the training data
model_Random_Forest = RandomForestClassifier()
model_Random_Forest.fit(X_train, Y_train)





# Make predictions on validation dataset
prediction_Random_Forest = model_Random_Forest.predict(X_test)



# Pickle model
pd.to_pickle(model_Random_Forest,r'random_forest.pickle')


# Unpickle model
model_Random_Forest = pd.read_pickle(r'random_forest.pickle')


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
result = model_Random_Forest.predict([[Age, Sex,Chest_Pain, Rest_BP, Cholestrol,Fast_BS,Rest_ECG,Max_Heart_Rate,Exercise,ExertoRest,Slope,No_Major_Vessels,Thal]])  # input must be 2D array
print(result)