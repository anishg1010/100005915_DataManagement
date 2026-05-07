import pandas as pd

def process_it_employees(df):
    avg_salary = df['Salary'].mean()
    
    #Finding the oldest employee in the whole company
    oldest_index = df['Age'].idxmax()
    
    oldest_name = df.loc[oldest_index, 'Employee_Name'] 
    oldest_dept = df.loc[oldest_index, 'Department']
    
    #Filtering the dataset to ONLY show the IT department
    filtered_df = df[df['Department'] == 'IT'].copy()
    
    filtered_df['Average_Salary_All_Employees'] = avg_salary
    filtered_df['Oldest_Employee_Name'] = oldest_name
    filtered_df['Oldest_Employee_Department'] = oldest_dept
    
    return filtered_df

def get_output_schema():
    return pd.DataFrame({
        'Employee_ID': prep_string(),
        'Employee_Name': prep_string(),
        'Department': prep_string(),
        'Age': prep_int(),
        'Salary': prep_decimal(),
        'Hire_Date': prep_string(),
        'City': prep_string(),
        'Average_Salary_All_Employees': prep_decimal(),
        'Oldest_Employee_Name': prep_string(),
        'Oldest_Employee_Department': prep_string()
    })