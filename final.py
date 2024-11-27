import re

def read_file(file_path):
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
                parts_of_address = address_full.split(",")
                street_num = parts_of_address[0]
                street_name = parts_of_address[1] + " " + parts_of_address[2]
                full_address = street_num + ", " + street_name + ", " + state

                # Extract the make and model
                make, model = make_model.split(" ", 1)  # Split only on the first space

                # Create a list with all required fields
                new_list = [[street_num, street_name, state], license_plate, make, model, vin, color]
                result_dict[ssn] = new_list

    color_criteria = 'White'
    make_criteria = 'Toyota'
    model_criteria = 'Camry'
    state_criteria = 'Virginia'
    filtered_dict = {}

    # Filter the dictionary based on criteria
    for ssn in result_dict:
        info = result_dict[ssn]
        if (info[5].lower() == color_criteria.lower() and  # Check color
                info[2].lower() == make_criteria.lower() and  # Check make
                info[3].lower() == model_criteria.lower() and  # Check model
                info[0][-1].lower() == state_criteria.lower()):  # Check state (last part of the address)
            filtered_dict[ssn] = info

    # Call the function to write filtered data to a file
    write_culprit_data(filtered_dict)

    return filtered_dict


def write_culprit_data(filtered_dict):
    with open("culprit.txt", "w") as file:
        for ssn, info in filtered_dict.items():
            # Write SSN on the first line
            file.write(ssn + "\n")

            # Build the full address
            street_num = info[0][0]
            street_name = info[0][1]
            state = info[0][2]
            full_address = street_num + ", " + street_name + ", " + state

            # Write the address on the second line
            file.write(full_address + "\n")

            # Write the license plate on the third line
            file.write(info[1] + "\n")

            # Add a blank line to separate entries
            file.write("\n")


# Example usage
filtered_data = read_file("v1_data.txt")
print(filtered_data)
