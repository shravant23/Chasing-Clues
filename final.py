import re


def read_file(file_path):
    result_list = []
    result_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Extract the license plate from the first 8 characters
            license_plate = line[:8]

            # Check if the license plate matches the criteria
            if re.search(r"^(?=.*D)(?=.*6)(?=.*7)", license_plate):
                # Split the line into fields
                data_list = line.strip().split("\t")

                # Assign variables to each field based on the new format
                license_plate = data_list[0]
                state = data_list[1]
                make_model = data_list[2]
                color = data_list[3]
                vin = data_list[4]
                ssn = data_list[5]
                address_full = data_list[6]

                # Extract the make and model
                make, model = make_model.split(" ", 1)  # Split only on the first space

                # Split the address into its components
                full_address = address_full.split(",")
                full_address.append(state)



                # Create the new list format
                new_list = [full_address, license_plate, make, model, vin, color]

                # Append the new list to the result list
                result_list.append(new_list)
                result_dict[ssn] = new_list

    # Print each list on a new line
    color_criteria = 'White'
    make_criteria = 'Toyota'
    model_criteria = 'Camry'
    state_criteria = 'Virginia'
    filtered_dict = {}
    for ssn in result_dict:
        info = result_dict[ssn]
        if (info[5].lower() == color_criteria.lower() and  # Check color
                info[2].lower() == make_criteria.lower() and  # Check make
                info[3].lower() == model_criteria.lower() and  # Check model
                info[0][-1].lower() == state_criteria.lower()):  # Check state (last part of the address)
            filtered_dict[ssn] = info
    return filtered_dict



# Example usage:
print(read_file("v1_data.txt"))