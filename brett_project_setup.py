"""
Module: brett_project_setup

Purpose: Provide functions to script project folders (and demonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Brett Vrtachnik

"""

#####################################
# Import Modules at the Top
#####################################

# Import modules from standand library
# TODO: Import additional modules as needed
import pathlib
import utils_bvrtachnik
import time

# Import local modules
# import utils_bvrtachnik 


#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string

    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # TODO: Implement the actual folder creation logic
    for year in range(start_year, end_year +1):
        year_folder = data_path.joinpath(str(year)) # Path to the year subfolder
        year_folder.mkdir(exist_ok=True)    # Create the folder (ignore if it exists)
        print(f"Created folder: {year_folder}")        


  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
   
   '''
   Create folders from a given list of names

   Arguments: 
   folder_list -- a list of folder names
   to_lowercase -- whether to convert folder names to lowercase (optional)
   remove_spaces -- whether to remove spaces from folder name (optional)
   '''

   # Log function and call its arguments 
   print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")

   # Loop through the folder names in the list
   for folder_name in folder_list:
        # Transform the folder name based on the options
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "")

        # Create the folder   
        folder_path = data_path.joinpath(folder_name) 
        folder_path.mkdir(exist_ok=True) # Create the folder if it doesn't exist
        print(f"Created folder: {folder_path}")



#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:

    '''
    Create a function to created prefixed folders by transforming a list of names
    and combining each with a prefix 

    Arguments:
    folder_list -- a list of folder names to be created and prefixed
    prefix -- the prefix to be added to the beginning of each folder name
    '''

    # Log the function and its arguments
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

    # Loop through the folder list, applying the prefix and creating the folder
    for folder_name in folder_list:
        prefixed_name = f"{prefix}{folder_name}" # Add the prefix to the folder name
        folder_path = data_path.joinpath(prefixed_name) # Create the full path with the prefixed name
        folder_path.mkdir(exist_ok=True) # Create the folder (if it doesn't exist)
        print(f"Created folder: {folder_path}")
  


#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:

    '''
    Create folders periodically at specified interval (every 5 seconds)
    
    Arguments: 
    duration_seconds -- amount of time between folders being creations
    '''

    # Log the function and its arguments
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

    # Loop to create a folder at specified interval (duration_seconds)
    for i in range(5): # Create 7 folders (you can adjust later)
        folder_name = f"folder{i +1}" # Generate folder name: folder1, folder2, etc.
        folder_path = data_path.joinpath(folder_name) # Create the full path
        folder_path.mkdir(exist_ok=True) # Create the folder u(if it doesn't exist already)
        print(f"Created folder: {folder_path}")

        time.sleep(duration_seconds) # Wait for the specified interval before created another folder


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_bvrtachnik.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    
    # Call function 2 to create folders with transformation options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.