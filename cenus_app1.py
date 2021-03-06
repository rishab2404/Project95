# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	census_df = pd.read_csv("adult.csv",header=None)
	census_df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(census_df.shape[1]):
	  census_df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	census_df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	census_df['native-country'] = census_df['native-country'].replace(' ?',np.nan)
	census_df['workclass'] = census_df['workclass'].replace(' ?',np.nan)
	census_df['occupation'] = census_df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	census_df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	census_df.drop(columns='fnlwgt',axis=1,inplace=True)

	return census_df

census_df = load_data()

st.set_option('deprecation.showPyplotGlobalUse', False)

# Write the code to design the web app

# Add title on the main page and in the sidebar.
st.title("CENSUS DATA WEB APP")
st.sidebar.title(" Visualisation Web App")

# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox("Show raw data"):
  st.subheader("Census Data set")
  st.dataframe(census_df)
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.sidebar.subheader("Visualisation selector")


# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plot_list=st.sidebar.multiselect("select the charts or plots ",("Boxplot","Piechart","Countplot"))


# Display pie plot using matplotlib module and 'st.pyplot()'
if "Piechart" in plot_list:
  plt.figure(figsize=(16,8))
  plt.title("Distribution of records for income-groups")
  pie_data=census_df["income"].value_counts()
  plt.pie(pie_data,labels=pie_data.index,autopct="%1.2f%%")
  st.pyplot()

  plt.figure(figsize=(16,8))
  plt.title("Distribution of records for gender group")
  gender_data=census_df["gender"].value_counts()
  plt.pie(gender_data,labels=gender_data.index,autopct="%1.2f%%")
  st.pyplot()


# Display box plot using matplotlib module and 'st.pyplot()'
if "Boxplot" in plot_list:
    st.subheader("Boxplot")
    column=st.sidebar.selectbox("Select the columns for boxplot",("income","gender"))
    plt.figure(figsize=(16,8))
    plt.title(f"Boxplot for {column}")
    sns.boxplot(census_df[column],census_df["hours-per-week"])
    st.pyplot()

# Display count plot using seaborn module and 'st.pyplot()' 
if "Countplot" in plot_list:
  st.subheader("Count plot for distrubution of records for unique workclass group")
  sns.countplot(x="workclass",data=census_df)
  st.pyplot()