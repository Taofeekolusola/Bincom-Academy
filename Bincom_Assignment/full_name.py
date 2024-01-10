# Define the name
full_name = "Olusola Taofeek Adeshina"
#create and write to the text file
with open('full_name.txt', 'w') as file:
    file.write(full_name)
print("Text file created successfully!")

# Open and read the content of the text file
with open('full_name.txt', 'r') as file:
    full_name = file.read().strip()

# Split the full name into parts
name_parts = full_name.split()
# Extract first name, surname, and last name
surname = name_parts[0]
first_name = name_parts[-2] 
last_name = name_parts[-1]

# Print the extracted names
print(f"First Name: {first_name}")
print(f"Surname: {surname}")
print(f"Last Name: {last_name}")
