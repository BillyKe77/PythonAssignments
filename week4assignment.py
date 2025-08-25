def modify_file(input_path, output_path):
    try:
        # Reading the original file
        with open(input_path, 'r') as infile:
            content = infile.read()

        # Modifying the content by converting to uppercase
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_path, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_path}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except PermissionError:
        print(f" Error: No permission to read '{input_path}'.")
    except Exception as e:
        print(f" Unexpected error: {e}")

# Prompting user for file paths
input_path = input("Enter the path of the input file: ")
output_path = input("Enter the path for the output file: ")
modify_file(input_path, output_path)

