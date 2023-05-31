import csv
import os

def merge_csv_files(directory, output_file):
    # Get a list of CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    total_files = len(csv_files)
    print(f"Total CSV files found: {total_files}")

    # Open the output file in write mode
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Loop through each CSV file
        for i, file in enumerate(csv_files, start=1):
            with open(os.path.join(directory, file), 'r') as infile:
                reader = csv.reader(infile)

                # Skip the first row of each CSV file
                next(reader)

                # Write the remaining rows to the output file
                writer.writerows(reader)

            print(f"Merged {file}. ({i}/{total_files})")

    print("CSV files merged successfully.")

# Directory containing CSV files
csv_directory = 'PATH'

# Output file path
output_file = 'PATH/combined.csv'

# Merge CSV files and remove the first row
merge_csv_files(csv_directory, output_file)
