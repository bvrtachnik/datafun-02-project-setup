"""
Module: utils_bvrtachnik

Purpose: Reusable Module for My Analytics Projects
Course: Data Analytics Fundamentals

Description: This module provides a byline for my analytics projects summarizing key data,
such as client satisfaction and local average annual temperature. 
When we work hard to write useful code, we want it to be reusable.

Author: Brett Vrtachnik

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
has_international_clients: bool = True
is_privately_held: bool = True

# declare an integer variable 
years_in_operation: int = 10
number_of_employees: int = 30

# declare a floating point variable
average_client_satisfaction: float = 4.7
average_local_annual_temperature: float = 70.5

# declare a list of strings
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
languages_used: list = ["SQL", "GitHub", "Python"]

# declare a list of numbers so we can illustrate statistics skills
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
local_annual_temperatures: list = [69.4, 74.2, 74.1, 72.3, 67.1, 69.7, 69.3, 68.0, 72.4, 68.5]

# Client satisfaction statistics
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Local annual temperature statistics
min_temperature: float = min(local_annual_temperatures)
max_temperature: float = max(local_annual_temperatures)
mean_temperature: float = statistics.mean(local_annual_temperatures)
stdev_temperature: float = statistics.stdev(local_annual_temperatures)


# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:                  {has_international_clients}
Is Privately Held:                          {is_privately_held}
Number of Employees:                        {number_of_employees}
Years in Operation:                         {years_in_operation}
Skills Offered:                             {skills_offered}
Languages Used:                             {languages_used}
Client Satisfaction Scores:                 {client_satisfaction_scores}
Minimum Satisfaction Score:                 {min_score}
Maximum Satisfaction Score:                 {max_score}
Mean Satisfaction Score:                    {mean_score:.2f}
Standard Deviation of Satisfaction Scores:  {stdev_score:.2f}
Local Annual Temperatures:                  {local_annual_temperatures}
Minimum Annual Temperature:                 {min_temperature}
Maximum Annual Temperature:                 {max_temperature}
Mean Annual Temperature:                    {mean_temperature}
Standard Deviation of Annual Temperature:   {stdev_temperature:.2f}

"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()
