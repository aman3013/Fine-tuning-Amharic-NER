import os

# Define the directory containing the .conll files
directory = '../notebooks/CONLL'

# Output file name
output_file = 'merged_file.conll'

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file ends with .conll
        if filename.endswith('.conll'):
            file_path = os.path.join(directory, filename)  # Create the full path for each file
            try:
                # Open each input file in read mode
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # Read and write the content of each file to the output file
                    outfile.write(infile.read())
                    outfile.write('\n')  # Optional: Add a newline after each file
            except FileNotFoundError:
                print(f"File {file_path} not found. Please check the file name and path.")
            except Exception as e:
                print(f"An error occurred while processing {file_path}: {e}")

print(f"Successfully merged all .conll files into {output_file}.")
