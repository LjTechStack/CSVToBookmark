# Bookmark CSV Parser
This is a Python script that parses a bookmark CSV file and generates an HTML file representing the bookmark structure. The script reads the CSV file, processes the data, and writes the HTML output file.

### Prerequisites
Python 3.x
### Usage
Ensure you have Python 3.x installed on your system.
Download or clone the script to your local machine.
Open a terminal or command prompt and navigate to the directory where the script is located.
Run the following command:
|shell
python bookmark_parser.py <input_directory>
Replace <input_directory> with the path to the directory containing the bookmark CSV files you want to process.

### Dependencies
The script requires the following Python modules:

csv: This module provides functionality for reading and writing CSV files.
os: This module provides a way to interact with the operating system, allowing file and directory operations.
sys: This module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
### Constants
TAB_DELIMITER: A constant representing the tab delimiter used in the CSV file.
TYPE: A constant representing the "type" column header in the CSV file.
PARENT: A constant representing the "parent" column header in the CSV file.
TITLE: A constant representing the "title" column header in the CSV file.
URL: A constant representing the "url" column header in the CSV file.
### Functions
parse_header_data(header): Parses the header of the CSV file and returns a dictionary mapping header items to their respective indices.
process_csv_data(csv_file, header_map): Processes the CSV data and returns two dictionaries: bookmark_dict and bookmark_object. bookmark_dict represents the bookmark hierarchy, and bookmark_object contains information about individual bookmarks.
isFolder(value, bookmark_dict): Checks if a value represents a folder in the bookmark hierarchy.
write_header(file, title): Writes the HTML header element for a bookmark folder.
write_folder(file, title): Writes the HTML element for a bookmark folder.
write_item(file, title, url): Writes the HTML element for a bookmark item.
write_closing_group(file): Writes the closing HTML tag for a bookmark folder.
write_end_file(file): Writes the closing HTML tags for the bookmark file.
parse_values(bookmark_dict, bookmark_object, key, values, visited, counter, file): Recursively parses the bookmark hierarchy and writes the corresponding HTML elements.
write_bookmark_elements(bookmark_dict, bookmark_object, file): Writes the HTML elements for the entire bookmark structure.
write_bookmark_header(file): Writes the HTML header for the bookmark file.
parse_bookmark_file(root, csv_file_name): Parses a bookmark CSV file and generates the HTML output file.
loop_input_directory(input_dir): Loops through the files in the input directory and processes the bookmark CSV files.
### Example

python bookmark_parser.py input_directory
Replace input_directory with the path to the directory containing your bookmark CSV files. The script will process the files and generate an HTML file named custom_bookmark.html in the output directory.

Note: Make sure the bookmark CSV files follow the expected format with the correct column headers: "type", "parent", "title", and "url".# CSVToBookmark