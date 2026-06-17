import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st
data=pd.read_csv("cleaned_jobs.csv")
#st.title("Job Market Analytics Dashboard")
st.markdown("<h1 style='color:#1E88E5;'>Job Market Analytics Dashboard</h1>",unsafe_allow_html=True)

#add sidebar filters
st.sidebar.title("Job Dashboard Filters")
selected_location=st.sidebar.selectbox("Select_Location",["All"]+list(data["Location"].unique()))
selected_industry=st.sidebar.selectbox("Select_industry",["All"]+list(data["Industry"].unique()))
selected_sector=st.sidebar.selectbox("Select_sector",["All"]+list(data["Sector"].unique()))
salary_type=st.sidebar.selectbox("salary_type",["All"]+list(data["Salary Type"].unique()))

#filter data
filtered_data=data
if selected_location != "All":
    filtered_data=filtered_data[filtered_data["Location"]==selected_location]
if selected_industry != "All":
    filtered_data=filtered_data[filtered_data["Industry"]==selected_industry]
if selected_sector != "All":
    filtered_data=filtered_data[filtered_data["Sector"]==selected_sector]
if salary_type != "All":
    filtered_data=filtered_data[filtered_data["Salary Type"]==salary_type]

#kpi 
try:
    data["avg_salary"] = data["avg_salary"].astype(int)
    total_jobs=len(filtered_data)
    total_company=filtered_data["Company Name"].nunique()
    unique_job=filtered_data["Job Title"].nunique()
    average_salary=filtered_data["avg_salary"].mean()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("TOTAL JOB OPENING:",total_jobs)
    with col2:
        st.metric("TOTAL COMPANY HIRING",total_company)
    with col3:
        st.metric("UNIQUE JOB ROLE",unique_job)
    with col4:
        st.metric("average salary","$"+str(int(round(average_salary))))
except:
    st.write("there is no matched records")
    st.stop()
    
#dataset preview
st.subheader("Dataset Preview")
st.dataframe(filtered_data.head(20))

#charts
#location
fig1=plt.figure(figsize=(7,4))
top_location=filtered_data["Location"].value_counts().head(10)
plt.bar(top_location.index,top_location.values,color="green")
plt.title("top hiring location",fontsize=16)
plt.xlabel("locations",fontsize=12)
plt.ylabel("job count",fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()


#industry
fig2=plt.figure(figsize=(7,4))
top_hiring_industry=filtered_data["Industry"].value_counts().head(10)
#plt.figure(figsize=(10,6))
sns.barplot(x=top_hiring_industry.values,y=top_hiring_industry.index,color="red")
plt.title("top hiring industry",fontsize=16)
plt.xlabel("job count",fontsize=12)
plt.ylabel("industry",fontsize=12)
plt.tight_layout()


#sector chart
fig3=plt.figure(figsize=(7,4))
top_hiring_sector=filtered_data["Sector"].value_counts().head(10)
sns.barplot(x=top_hiring_sector.values,y=top_hiring_sector.index,color="yellow")
plt.title("top hiring sector",fontsize=16)
plt.xlabel("sector",fontsize=12)
plt.ylabel("job count",fontsize=12)
plt.tight_layout()


#salary estimation
fig4=plt.figure(figsize=(7,4))
top_salary=filtered_data["Salary Estimate"].value_counts().head(10)
# plt.figure(figsize=(10,6))
sns.barplot(x=top_salary.index,y=top_salary.values,color="purple")
plt.title("top salary estimates",fontsize=16)
plt.xlabel("job count",fontsize=12)
plt.ylabel("salary",fontsize=12)
plt.tight_layout()

#rating
fig5=plt.figure(figsize=(7,4))
top_rating=filtered_data["Rating"].value_counts().head(10)
# plt.figure(figsize=(12,5))
sns.histplot(filtered_data["Rating"],bins=10,color="orange")
plt.title("top salary rating",fontsize=16)
plt.xlabel("rating",fontsize=12)
plt.ylabel("company_count",fontsize=12)
plt.tight_layout()


col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)
with col1:
    st.pyplot(fig3)
with col2:
    st.pyplot(fig4)
with col1:
    st.pyplot(fig5)
    

st.markdown("created by manjula")

st.download_button("Download Filtered Data",filtered_data.to_csv(index=False),file_name="filtered_jobs.csv")


