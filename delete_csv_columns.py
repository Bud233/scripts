import os
import csv

def process_csv_files(directory, num_columns):
    # Get the list of CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    
    # Loop through each CSV file
    for file in csv_files:
        file_path = os.path.join(directory, file)
        print("Processing file:", file_path)
        
        # Read the CSV file
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
        
        # Delete columns beyond the specified number
        modified_rows = [row[:num_columns] for row in rows]
        
        # Write the modified data back to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(modified_rows)
        
        print("File processed successfully:", file_path)
    
    print("All CSV files processed.")

# Check if the config file exists
if os.path.exists("config.txt"):
    with open("config.txt", "r") as file:
        config_data = file.readlines()
    
    # Check if there is existing data in the config file
    if config_data:
        default_directory = config_data[0].strip()
        default_columns = int(config_data[1].strip())
        use_default = input(f"Use default settings? Directory: '{default_directory}', Columns: '{default_columns}' (y/n): ")
        
        if use_default.lower() == 'y':
            directory_path = default_directory
            num_columns = default_columns
        else:
            # Prompt the user to input the directory path
            directory_path = input("Enter the directory path: ")
            
            # Check if the path exists and save it for future runs
            if os.path.exists(directory_path):
                with open("config.txt", "w") as file:
                    file.write(directory_path + '\n')
                    num_columns = int(input("Enter the number of columns to save (default is 12): "))
                    file.write(str(num_columns))
            else:
                print("Invalid directory path.")
                exit()
    else:
        # Prompt the user to input the directory path
        directory_path = input("Enter the directory path: ")
        
        # Check if the path exists and save it for future runs
        if os.path.exists(directory_path):
            with open("config.txt", "w") as file:
                file.write(directory_path + '\n')
                num_columns = int(input("Enter the number of columns to save (default is 12): "))
                file.write(str(num_columns))
        else:
            print("Invalid directory path.")
            exit()
else:
    # Prompt the user to input the directory path
    directory_path = input("Enter the directory path: ")
    
    # Check if the path exists and save it for future runs
    if os.path.exists(directory_path):
        with open("config.txt", "w") as file:
            file.write(directory_path + '\n')
            num_columns = int(input("Enter the number of columns to save (default is 12): "))
            file.write(str(num_columns))
    else:
        print("Invalid directory path.")
        exit()

# Call the function to process the CSV files in the directory
process_csv_files(directory_path, num_columns)
