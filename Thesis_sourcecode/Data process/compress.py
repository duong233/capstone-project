import os
import csv
from loguru import logger

folder_path = '/home/bkcs/Desktop/Data/Timestamp-Bytecode'  # Replace with the path to your folder
csv_file_path = 'timestamp.csv'  # Replace with the desired path for the output CSV file

sub_path = os.listdir(folder_path)

for index,path in enumerate(sub_path):
    logger.info(f'Processing')
    cnt = 1
    # Open the CSV file in write mode
    with open(csv_file_path, 'a+', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(['BYTECODE', 'ADDRESS'])

        new_path = f'{folder_path}/{path}'

        files = os.listdir(new_path)
        total = len(files)
        # Iterate over the files in the folder
        for filename in files:
            if filename.endswith('.txt'):  # Only process TXT files
                file_path = os.path.join(new_path, filename)
                
                # Read the content of the file
                with open(file_path, 'r') as txt_file:
                    file_content = txt_file.read()
                
                # Write the file detail and name to the CSV file
                writer.writerow([file_content, filename])
                logger.info(f'Processing file {cnt}/{total}')
                cnt += 1

logger.info('Done')