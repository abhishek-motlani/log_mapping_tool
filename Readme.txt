log_mapping_tool

Take Home Assessment by Illumio

Usage
Prerequisites
1. Python 3.x installed on your system.
2. csv installed(mostly installed by default)
3. log file in txt file format
4. A CSV file (lookup_table.csv) containing the necessary tag mappings.

Running the Script
1. Clone the Repository(https://github.com/abhishek-motlani/log_mapping_tool/tree/main)
2. Install python
3. Replace test.txt with your input log file if necessary
4. run command python log_mapping.py in terminal
5. Output: The modified log with tags will be saved in tagged_output.txt. Counts of tags and port/protocol combinations will be saved in output.csv

The whole working of code
This Python script processes a log file containing network data and performs the following tasks:
1. Protocol Number Mapping: It maps protocol numbers to their corresponding protocol names using a predefined dictionary.
2. Tag Lookup: It assigns tags to log entries based on destination port and protocol by referencing a CSV file (lookup_table.csv).
3. Log File Modification: The script appends the assigned tags to each line of the input log file (test.txt) and writes the modified lines to an output file (tagged_output.txt).
4. Counting: It counts the occurrences of each tag and each port/protocol combination in the log file.
5. Output: The results are saved in a CSV file (output.csv), which contains the counts of tags and port/protocol combinations.

Assumptions
1. Log Data Format: The script is designed to handle log data in default format, and it assumes that the input data will consistently follow this format.
2. Protocol Mapping: The script uses a custom dictionary to map protocol numbers to protocol names for tag lookup. Example mappings include `tcp-6`, `udp-17`, and `icmp-1`. But in future we can use different library or function for mapping all protocols.
3. Input File Consistency: The script assumes that the input data, including the lookup table (`lookup_table.csv`), will be formatted consistently as expected by the script.
4. File Integrity: To preserve the integrity of the original log file, the script creates a separate output file (`tagged_output.txt`) with the tagged logs, rather than modifying the original file directly.
5. Combined Output: The script generates a single output file (`output.csv`) that contains both tag counts and port, protocol combination counts.
   

Unit Testing
This project includes unit tests using Python's built-in unittest framework to verify the functionality of the log mapping tool. The tests ensure that each function behaves as expected and that the overall system produces the correct outputs.

Test Cases Overview
1. test_map_protocol_known: Verifies that the map_protocol function correctly maps a known protocol number to its corresponding protocol name.
Example: map_protocol(6) should return "tcp".
2. test_lookup_table: Checks that the lookup_table function correctly extracts tags from the lookup_table.csv file when the destination port and protocol match.
Example: lookup_table(25, "tcp", 'lookup_table.csv') should return "sv_P1".
3. test_lookup_table_not_found: Ensures that the lookup_table function returns "Untagged" when no matching entry is found in the lookup table.
Example: lookup_table(1, "HTTP", 'lookup_table.csv') should return "Untagged".
4. test_log_mapping_output: Verifies that the log_mapping function correctly processes the log file and produces the expected tag counts and port/protocol combinations.
This test checks that the correct tags and port/protocol combinations appear in the output.

Potential Improvements
1. Efficiency Enhancement: If the lookup table is frequently accessed for tag mapping, efficiency could be improved by indexing the dst_port and protocol fields using a library like pandas, allowing for faster tag retrieval.
2. Batch Processing: If the log file size increases, the script can be modified to process logs in batches (e.g., 10,000 rows per batch) to manage memory usage more efficiently and avoid excess memory consumption.
3. Enhanced Error Handling: In future we can implement additional error handling to check the integrity of the input data, such as verifying that the log file contains the expected fields and formats. Add checks to ensure that input files, such as the log file and lookup table, are not empty before processing begins. Include handling for common issues like missing files, incorrect data formats, and other potential data-related errors to make the script more robust.

