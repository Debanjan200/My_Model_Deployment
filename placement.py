import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_set=pd.read_csv("collegePlace.csv")

def lower(text):
    text=text.lower()
    return text

data_set["Gender"]=data_set["Gender"].apply(lower)
data_set["Stream"]=data_set["Stream"].apply(lower)

from sklearn.preprocessing import LabelEncoder
stream_encoder=LabelEncoder()
data_set["Stream"]=stream_encoder.fit_transform(data_set["Stream"].values)
gender_encoder=LabelEncoder()
data_set["Gender"]=gender_encoder.fit_transform(data_set["Gender"].values)

x=data_set.iloc[:,:-1].values
y=data_set.iloc[:,-1].values

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x=sc_x.fit_transform(x)

from sklearn.svm import SVC
svc_classifier=SVC(kernel="rbf",random_state=42)
svc_classifier.fit(x,y)

# age=int(input("Enter Age:"))
# gender=gender_encoder.transform([input("Enter Gender:").lower()])
# stream=stream_encoder.transform([input("Enter Stream:").lower()])
# intership=int(input("Enter the number of intership you have done(in number):"))
# cgpa=int(input("Enter cgpa:"))
# hostel=input("Enter you have hostel(yes/no):").lower()
# if hostel=="yes":
#     hostel=1

# else:
#     hostel=0

# backloag=int(input("Enter how many backloag you have(in number):"))

# test=[[age,gender,stream,intership,cgpa,hostel,backloag]]
# res=svc_classifier.predict(sc_x.transform(test))

# if res[0]==1:
#     print("You have chance to place in a company")

# elif res[0]==0:
#     print("You have less chance to place in a company")

