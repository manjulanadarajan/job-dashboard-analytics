import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=pd.read_csv(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\data\cleaned_jobs.csv")
print(data.head)
print(data.shape)
print(data.columns)
print(data.info())
print(data.isnull().sum())
print(data.describe())
salary=data["Salary Estimate"]
#print(salary)
# print(salary.unique())
# print(salary[salary == -1].sum())
# print(data[data["Job Title"] == -1].sum())
# print((data["Sector"]=="Unknown").value_counts())
# print((data["Revenue"]=="Unknown").value_counts())
# print((data["Easy Apply"]=="-1").value_counts())
# print((data["Job Title"]=="-1").value_counts())
# print((data["Job Title"]=="Unknown").value_counts())
# print((data["Job Title"]=="").value_counts())
# print(data["Job Title"].isnull().sum())
# print((data["Salary Estimate"]=="-1").value_counts())
# print((data["Salary Estimate"]=="Unknown").value_counts())
# print((data["Salary Estimate"]=="").value_counts())
# print(data["Salary Estimate"].isnull().sum())
# print((data["Job Description"]=="-1").value_counts())
# print((data["Job Description"]=="Unknown").value_counts())
# print((data["Job Description"]=="").value_counts())
# print(data["Job Description"].isnull().sum())
# print((data["Rating"]==-1).value_counts())
# print((data["Rating"]=="Unknown").value_counts())
# print((data["Rating"]=="").value_counts())
# print(data["Rating"].isnull().sum())
# print((data["Company Name"]=="1").value_counts())
# print((data["Company Name"]=="Unknown").value_counts())
# print((data["Company Name"]=="").value_counts())
# print(data["Company Name"].isnull().sum())
# print((data["Location"]=="-1").value_counts())
# print((data["Location"]=="Unknown").value_counts())
# print((data["Location"]=="").value_counts())
# print(data["Location"].isnull().sum())
# print((data["Headquarters"]=="-1").value_counts())
# print((data["Headquarters"]=="Unknown").value_counts())
# print((data["Headquarters"]=="").value_counts())
# print(data["Headquarters"].isnull().sum())
# print((data["Size"]=="-1").value_counts())
# print((data["Size"]=="Unknown").value_counts())
# print((data["Size"]=="").value_counts())
# print(data["Size"].isnull().sum())
# print((data["Founded"]==-1).value_counts())
# print((data["Founded"]=="Unknown").value_counts())
# print((data["Founded"]=="").value_counts())
# print(data["Founded"].isnull().sum())
# print((data["Type of ownership"]==-1).value_counts())
# print((data["Type of ownership"]=="Unknown").value_counts())
# print((data["Type of ownership"]=="").value_counts())
# print(data["Type of ownership"].isnull().sum())
# print((data["Industry"]=="-1").value_counts())
# print((data["Industry"]=="Unknown").value_counts())
# print((data["Industry"]=="").value_counts())
# print(data["Industry"].isnull().sum())
# print((data["Sector"]=="-1").value_counts())
# print((data["Sector"]=="Unknown").value_counts())
# print((data["Sector"]=="").value_counts())
# print(data["Sector"].isnull().sum())
# print((data["Revenue"]=="-1").value_counts())
# print((data["Revenue"]=="Unknown").value_counts())
# print((data["Revenue"]=="").value_counts())
# print(data["Revenue"].isnull().sum())
# print((data["Competitors"]=="-1").value_counts())
# print((data["Competitors"]=="Unknown").value_counts())
# print((data["Competitors"]=="").value_counts())
# print(data["Competitors"].isnull().sum())
# print((data["Easy Apply"]=="-1").value_counts())
# print((data["Easy Apply"]=="Unknown").value_counts())
# print((data["Easy Apply"]=="").value_counts())
# print(data["Easy Apply"].isnull().sum())
# print(data.duplicated().sum())
# print(data["Company Name"].head())
# print(data["Company Name"].unique())
# print(data["Company Name"].value_counts())

# print(data["Salary Estimate"].head())
# print(data["Location"].unique())
# print(data["Location"].value_counts())
# print(data["Salary Estimate"].min())
# print(data["Salary Estimate"].max())
# data["Salary Estimate"] = data["Salary Estimate"].str.replace("(Glassdoor est.)","")
# print(data["Salary Estimate"].head())

                         #exploratry data analysis
print(data["Location"].value_counts().head(10))
#Which location has the highest number of job postings?  
top_location=data["Location"].value_counts().head(10)   
print(top_location.index[0],"has the highest number of job postings",top_location.values[0])
# 2. Which industry has the highest number of jobs?
data=data[data["Industry"]!='-1']
top_industry=data["Industry"].value_counts().head(10)
print(top_industry.index[0],"industry has the highest number of jobs",top_industry.values[0])

# 3. Which company appears most frequently in the dataset?
data=data[data["Company Name"]!='1']
data["Company Name"] = data["Company Name"].str[:-4]
top_company=data["Company Name"].value_counts().head(10)
print(top_company.index[0],"company appears most frequently in the dataset",top_company.values[0])



# 4. What are the most common salary ranges?
data1=pd.read_excel(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\data\yearly_salary.xlsx")
data1["Salary Estimate"] = data1["Salary Estimate"].str.replace("(Glassdoor est.)","")
most_common_salary=data1["Salary Estimate"].value_counts().head(10)
print(most_common_salary.index[0],"is the most common salary range with",most_common_salary.values[0],"job postings")

# 5. Which sector has the highest number of jobs?


# 6. What is the distribution of company ratings?

# 7. Which locations offer the highest salaries?

# 8. Which industries provide the highest salary estimates?

# 9. What are the most common company sizes?

# 10. Which type of ownership appears most frequently?

# 11. What is the average salary range in the dataset?

# 12. Which companies have the highest ratings?

# 13. Which sectors dominate the Data Science job market?

# 14. How are salaries distributed across different locations?

# 15. Which locations have the highest concentration of Data Science jobs?

            

                   #visualization
#top hiring companies
top_companies=data["Company Name"].value_counts().head(10)
plt.figure(figsize=(12,5))
sns.barplot(x=top_companies.values,y=top_companies.index)
plt.title("top hiring companies")
plt.xlabel("job count")
plt.ylabel("company")
plt.savefig(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\charts\top_hiring_companies.png")
plt.show()


#location
# top_location=data["Location"].value_counts().head(10)
# plt.figure(figsize=(12,5))
# plt.bar(top_location.index,top_location.values)
# plt.title("top hiring location")
# plt.xlabel("locations")
# plt.ylabel("job count")
# plt.xticks(rotation=45)
# plt.savefig(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\charts\top_location.png")
# # plt.plot(x,y)
# plt.show()


# #industry
# data = data[data["Industry"] != "-1"]
# top_hiring_industry=data["Industry"].value_counts().head(10)
# plt.figure(figsize=(10,6))
# sns.barplot(x=top_hiring_industry.values,y=top_hiring_industry.index)
# plt.title("top hiring industry")
# plt.xlabel("industry")
# plt.ylabel("job count")
# plt.savefig(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\charts\top_hiring_industry.png")
# plt.show()

# #sector chart
# top_hiring_sector=data["Sector"].value_counts().head(10)
# plt.figure(figsize=(10,6))
# sns.barplot(x=top_hiring_sector.values,y=top_hiring_sector.index)
# plt.title("top hiring sector")
# plt.xlabel("sector")
# plt.ylabel("job count")
# plt.savefig(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\charts\top_hiring_sector.png")
# plt.show()

# #salary estimation
# data1=pd.read_excel(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\data\yearly_salary.xlsx")
# data1["Salary Estimate"] = data1["Salary Estimate"].str.replace("(Glassdoor est.)","")
# top_salary=data1["Salary Estimate"].value_counts().head(10)
# plt.figure(figsize=(10,6))
# sns.barplot(x=top_salary.index,y=top_salary.values)
# plt.title("top salary estimates")
# plt.xlabel("job count")
# plt.ylabel("salary")
# plt.savefig(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\charts\high_salary.png")
# plt.show()

# #rating
# data = data[data["Industry"] != "-1"]
# top_rating=data["Rating"].value_counts().head(10)
# plt.figure(figsize=(12,5))
# sns.histplot(data["Rating"],bins=10)
# plt.title("top salary rating")
# plt.xlabel("rating")
# plt.ylabel("company_count")
# # plt.xticks(rotation=45)
# plt.savefig(r"C:\Users\8121a\OneDrive\Desktop\job dashboard analytics\charts\rating_distribution.png")
# plt.show()




















