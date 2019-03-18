# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)

loan_status=data["Loan_Status"].value_counts()
plt.bar(["YES","NO"],data=loan_status,height=[10,100])


#Code starts here


# --------------
#Code starts here
property_and_loan=data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

#Changing the x-axis label
plt.xlabel('Property_Area')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Code ends here


# --------------


education_and_loan=data.groupby(by=["Education","Loan_Status"])
education_and_loan=education_and_loan.size().unstack()
property_and_loan.plot(kind='bar',figsize=(15,10))
plt.xlabel('Education')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)


# --------------
#Code starts here

graduate=data[data['Education'] == 'Graduate']

not_graduate=data[data['Education'] == 'Not Graduate']


graduate.plot(kind="density",label="graduate")


not_graduate.plot(kind="density",label="not_graduate")




#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3)= plt.subplots(nrows = 3 , ncols = 1)
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Application Income')

ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Cpapplicant Income')

data["TotalIncome"]=data["ApplicantIncome"]+data["CoapplicantIncome"]
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set_title('Total Income')





