# this is the python file for the solution of the problem statement basics
# importing the important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel('student_data.xlsx')

# solving the basics questions
# question 1: How many unique students are included in the dataset?
# answers
unique_students = data['Email ID'].nunique()
print(f'Total unique students: {unique_students}')

# question 2:What is the average GPA of the students?
# answer
average_gpa = data['CGPA'].mean()
print(f'Average GPA: {average_gpa}')

# question 3: What is the distribution of students across different graduation years?
# answer
grad_year_distribution = data['Year of Graduation'].value_counts()
print(grad_year_distribution)

# question 4: What is the distribution of students' experience with Python programming?
# answer
python_exp_distribution = data['Experience with python (Months)'].value_counts()
print(python_exp_distribution)

# question 5:What is the average family income of the student?
# answer
import re

# Function to clean and convert 'Family Income'
def clean_family_income(value):
    # Check if the value is a range like '2-3lakh'
    if '-' in value:
        # Extract the two numbers from the range
        range_values = re.findall(r'\d+', value)
        # Convert to integers and take the average
        return (int(range_values[0]) + int(range_values[1])) / 2
    else:
        # Extract the first number and ignore any non-numeric characters
        number = re.search(r'\d+', value)
        if number:
            return int(number.group(0))
        return np.nan  # Return NaN if no valid number is found

# Apply the function to clean the 'Family Income' column
data['Cleaned Family Income'] = data['Family Income'].apply(clean_family_income)

# Calculate the average family income after cleaning
average_income = data['Cleaned Family Income'].mean()
print(f'Average Family Income: {average_income} lakh')

# question 6:How does the GPA vary among different colleges? (Show top 5 results only)
# answer
gpa_by_college = data.groupby('College Name')['CGPA'].mean().sort_values(ascending=False).head(5)
print(gpa_by_college)

# question 7:Are there any outliers in the 'attendee status' & 'quantity' (number of courses completed)?
# answer
# Plot boxplot for attendee status
sns.boxplot(data=data, x='Attendee Status', y='Quantity')
plt.show()
# Checking for outliers using IQR
Q1 = data['Quantity'].quantile(0.25)
Q3 = data['Quantity'].quantile(0.75)
IQR = Q3 - Q1
outliers = data[(data['Quantity'] < (Q1 - 1.5 * IQR)) | (data['Quantity'] > (Q3 + 1.5 * IQR))]
print(f'Number of outliers in Quantity: {len(outliers)}')

# question 8: What is the average GPA for students from each city?
# answer
avg_gpa_by_city = data.groupby('City')['CGPA'].mean()
print(avg_gpa_by_city)

# now the moderate questions 

# question 10:How does the expected salary vary based on factors like 'GPA', 'Family income', 'Experience with Python (Months)'?
# answer
salary_factors = data[['CGPA', 'Family Income', 'Experience with Python (Months)', 'Expected Salary (Lac)']]
sns.pairplot(salary_factors)
plt.show()

correlation_salary = salary_factors.corr()
print(correlation_salary)

# question 11:Which event tends to attract more students from specific fields of study?
# answer
event_fields = data.groupby(['Events', 'Designation']).size().unstack().fillna(0)
print(event_fields)

# question 12:Do students in leadership positions during their college years tend to have higher GPAs or better expected salary?
# answer
leadership_gpa_salary = data.groupby('Leadership Skills')[['CGPA', 'Expected Salary (Lac)']].mean()
print(leadership_gpa_salary)

# question 13:Is there a correlation between leadership skills and expected salary of the students?
# answer
leadership_salary_corr = data[['Leadership Skills', 'Expected Salary (Lac)']].corr()
print(leadership_salary_corr)

# question 14:How many students are graduating by the end of 2024?
# answer
grad_2024 = data[data['Year of Graduation'] <= 2024].shape[0]
print(f'Students graduating by the end of 2024: {grad_2024}')

# question 15:Which promotion channel brings in more student participations for the event?
# answer
promotion_channel = data['How did you come to know about this event?'].value_counts()
print(promotion_channel)

# question 16:Find the total number of students who attended events related to Data Science?
# answer
data_science_events = data[data['Events'].str.contains('Data Science', case=False)]
total_data_science_students = data_science_events.shape[0]
print(f'Total students attended Data Science events: {total_data_science_students}')

# question 17:Do those who have a high CGPA and more experience with Python have high salary expectations?
# answer
high_cgpa_python = data[(data['CGPA'] > 8) & (data['Experience with Python (Months)'] > 12)]
avg_salary_high = high_cgpa_python['Expected Salary (Lac)'].mean()
print(f'Average expected salary for high CGPA & Python experience: {avg_salary_high}')

# question 18:How many students know about the event from their colleges? Which are the top 5 colleges?
# answer
known_from_college = data[data['How did you come to know about this event?'] == 'College']['College Name'].value_counts().head(5)
print(known_from_college)



