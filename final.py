import re

file = open("v1_data.txt", "r").read()

def read_file(file_path):
    result_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            license_plate = line[:8]
            if re.search(r"^(?=.*D)(?=.*6)(?=.*7)", license_plate):
                data_list = line.strip().split("\t")
                ssn = data_list[5]
                address = data_list[-1].split(",")
                result_dict[ssn] = [address] + data_list[1:5]





# Example usage:
print(read_file("v1_data.txt"))
