import re


def read_file(file_path):
   result_dict = {}


   # First loop: Process the file and build the result_dict
   with open(file_path, 'r') as file:
       for line in file:
           license_plate = line[:8]
           if re.search(r"^(?=.*D)(?=.*6)(?=.*7)", license_plate):
               data_list = line.strip().split("\t")  # Split the line by tabs
               ssn = data_list[5]  # SSN is the 6th element (index 5)
               address = data_list[1]  # The second element in the data_list is the address
               result_dict[ssn] = [address] + data_list[2:5]  # Store address first, followed by other data


   # Second loop: Filter the dictionary to only include entries where Virginia is in the address
   virginia_dict = {}
   for ssn in result_dict:
       address = result_dict[ssn][0]  # The first part of the data is the address
       if "Virginia" in address:  # Check if Virginia is part of the address
           virginia_dict[ssn] = result_dict[ssn]


   return virginia_dict




# Example usage:
print(read_file("v1_data.txt"))