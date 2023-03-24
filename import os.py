import os

# Define the file paths
input_file = "/home/islem/bfgminer"
output_file = "/home/islem/bfgminer"

# Open the input file in binary mode
with open(input_file, "rb") as f_in:
    # Read the contents of the input file
    contents = f_in.read()
    
    # Search for binary files
    binaries = [x for x in contents if x in range(128, 256)]
    
    # Create a new file to write the binary files
    with open(output_file, "wb") as f_out:
        # Write the binary files to the output file
        f_out.write(bytearray(binaries))
