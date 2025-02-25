#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function to calculate XOR checksum

import argparse
parser = argparse.ArgumentParser(description="Robust implementation of LT Codes encoding/decoding process.")
parser.add_argument("filename", help="file path of the file to split in blocks")
parser.add_argument("filenameOut", help="file path of the file to split in blocks")
args = parser.parse_args()


def calculate_xor_checksum(chunk):

    checksum = 0

    for byte in chunk:

        checksum ^= byte

    return checksum



# Function to process a binary file and append checksums

def process_file_with_checksums(input_file, output_file, chunk_size):

    with open(input_file, 'rb') as input_f, open(output_file, 'wb') as output_f:

        while True:

            # Read a chunk

            chunk = input_f.read(chunk_size)

            if not chunk:

                break

            # Calculate checksum

            checksum = calculate_xor_checksum(chunk)

            # Append checksum to chunk

            output_f.write(chunk + bytes([checksum]))



# Process the input binary file

#process_file_with_checksums(args.filename, args.filenameOut, 5)



# Step 2: Verify Checksum for Each Chunk

# This part verifies each chunk's checksum from the processed file.



# Function to read and verify checksums

def verify_chunks(file_path, chunk_size):

    with open(file_path, 'rb') as file:

        while True:

            # Read a chunk with its checksum

            chunk_with_checksum = file.read(chunk_size + 1)

            if not chunk_with_checksum:

                break

            # Separate data and checksum

            data_chunk = chunk_with_checksum[:-1]

            read_checksum = chunk_with_checksum[-1]

            # Recalculate checksum

            calculated_checksum = calculate_xor_checksum(data_chunk)

            # Verify

            if calculated_checksum == read_checksum:

                print("Checksum verification passed for chunk.")

            else:

                print("Checksum verification failed for chunk.")




# Step 1: Read the file in binary mode
def second_method(input_file, output_file):
    with open(input_file, 'rb') as file:

        binary_data = file.read()



    # Step 2: Process the binary data

    chunk_size = 32  # Define the size of each chunk

    indexed_data = bytearray()



    # Iterate over the binary data in chunks

    for index, start in enumerate(range(0, len(binary_data), chunk_size)):

        chunk = binary_data[start:start+chunk_size]  # Extract each chunk of binary data



        # Convert the current index into a 4-byte big-endian integer

        # This ensures that each chunk starts with its index as metadata

        index_bytes = index.to_bytes(4, byteorder='big')



        # Concatenate the index with the chunk

        indexed_chunk = index_bytes + chunk



        # Append the indexed chunk to the result bytearray

        indexed_data.extend(indexed_chunk)



    # Step 3: Write the modified data

    with open(output_file, 'wb') as file:

        file.write(indexed_data)



    # Step 4: Strip the index and compare

    # Read the modified file

    with open(output_file, 'rb') as file:

        modified_data = file.read()



    # Prepare to reconstruct the original data

    original_data_reconstructed = bytearray()



    # Iterate over the indexed chunks, stripping the index

    for start in range(0, len(modified_data), chunk_size + 4):

        # Each chunk now contains a 4-byte index at the start

        indexed_chunk = modified_data[start:start + chunk_size + 4]

        # Strip the 4-byte index

        original_chunk = indexed_chunk[4:]

        original_data_reconstructed.extend(original_chunk)



    # Step 5: Compare reconstructed data to the original data

    if original_data_reconstructed == binary_data:

        print("Success: The data matches the original!")

    else:

        print("Error: The data does not match the original!")


second_method(args.filename, args.filenameOut)



# Assume each original data chunk size was 5 bytes

#verify_chunks(args.filenameOut, 5)