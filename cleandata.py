import pandas as pd
data=pd.read_csv(r"C:\Users\8121a\Downloads\DataScientist.csv\DataScientist.csv")
                #SALARY ESTIMATION
data["Salary Type"] = data["Salary Estimate"].apply(lambda x: "Hourly" if "Per Hour" in str(x) else "Yearly")
data["Salary Estimate"]=data["Salary Estimate"].str.replace("$","")
data["Salary Estimate"]=data["Salary Estimate"].str.replace("(Glassdoor est.)","")
data["Salary Estimate"]=data["Salary Estimate"].str.replace("(Employer est.)","")
data["Salary Estimate"]=data["Salary Estimate"].str.replace("K","")
data["Salary Estimate"]=data["Salary Estimate"].str.replace("Per Hour(Glassdoor est.)","")
data["Salary Estimate"]=data["Salary Estimate"].str.replace("Per Hour","")
data["min_salary"]=data["Salary Estimate"].str.split("-").str[0]
data["max_salary"]=data["Salary Estimate"].str.split("-").str[1]
data["avg_salary"] = (data["min_salary"].astype(float)+data["max_salary"].astype(float)) / 2
#int(data["Salary Estimate"])
                               #rating
avg = data[data["Rating"] != -1]["Rating"].mean()
data["Rating"] = data["Rating"].replace(-1, avg)
                                #company
data = data[data["Company Name"] != "1"]
data["Company Name"] = data["Company Name"].str.rsplit(" ", n=1).str[0]
                                #headquarders
data["Headquarters"]=data["Headquarters"].replace("-1","Unknown Headquarters")
                                #size
data["Size"]=data["Size"].replace("-1","Unknown Size")
data["Size"]=data["Size"].replace("Unknown","Unknown Size")
                              #founded
data["Founded"]=data["Founded"].replace(-1,0)
                             #types of ownership
data["Type of ownership"]=data["Type of ownership"].replace("-1","Unknown ownership")
data["Type of ownership"]=data["Type of ownership"].replace("Unknown","Unknown ownership")
                           #industry
data["Industry"]=data["Industry"].replace("-1","Unknown industry")
                           #sector
data["Sector"]=data["Sector"].replace("-1","Unknown sector")
                           #Revenue
data["Revenue"]=data["Revenue"].replace("Unknown / Non-Applicable","Unknown Revenue")
data["Revenue"]=data["Revenue"].replace("-1","Unknown Revenue")
                           #competitor
data["Competitors"]=data["Competitors"].replace("-1","Unknown competitor")
                            #easy apply
data = data.drop("Easy Apply", axis=1)


data.to_csv(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\data\cleaned_jobs.csv",index=False)



