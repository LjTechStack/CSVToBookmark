import csv
import os
import sys

TAB_DELIMITER = "\t"
TYPE = "type"
PARENT = "parent"
TITLE = "title"
URL = "url"

BOOKMARK_OBJECT = {}
BOOKMARK_FOLDER_STRUC = {}


def parse_header_data(header):
    """Process header file of csv"""
    header_map = {}
    for index, header_item in enumerate(header):
        header_map[header_item] = index
    return header_map


def process_csv_data(csv_file, header_map):
    bookmark_dict = {}
    bookmark_object = {}
    """Process the csv data"""
    for line in csv.reader(csv_file, delimiter="\t"):
        if line[header_map[PARENT]] == 'None':
            bookmark_dict["root"] = []
            bookmark_dict["root"].append(line[header_map[TITLE]])
        else:
            # print(f"parent: {line[header_map[PARENT]]} has Content: {bookmark_dict.get(line[header_map[PARENT]])}")
            if bookmark_dict.get(line[header_map[PARENT]]) is None:
                bookmark_dict[line[header_map[PARENT]]] = []
                bookmark_dict[line[header_map[PARENT]]].append(line[header_map[TITLE]])
                # print("parent: " + str(header_map[PARENT]) + "title: " + str(header_map[TITLE]))
            else:
                bookmark_dict[line[header_map[PARENT]]].append(line[header_map[TITLE]])
        if len(line) != header_map[URL]:
            bookmark_object[line[header_map[TITLE]]] = {
                TITLE: line[header_map[TITLE]],
                URL: line[header_map[URL]],
            }
    return bookmark_dict, bookmark_object


def isFolder(value, bookmark_dict):
    if value in bookmark_dict.keys():
        return True
    return False


def write_header(file, title):
    file.write(f"<DT><H3 ADD_DATE=\"1682564679\" LAST_MODIFIED=\"1682570371\" PERSONAL_TOOLBAR_FOLDER=\"true\">{title}</H3>\n\t<DL><p>\n\t")


def write_folder(file, title):
    file.write(f"<DT><H3>{title}</H3>\n")
    file.write("<DL><p>\n")


def write_item(file, title, url):
    file.write(f"<DT><A HREF=\"{url}\">{title}</A>\n")


def write_closing_group(file):
        file.write("</DL><p>\n")


def write_end_file(file):
    file.write("</DL><p>")


def parse_values(bookmark_dict, bookmark_object, key, values, visited, counter, file):
    counter_current = counter
    for value in values:
        if value not in visited:
            counter_current += 1
            if isFolder(value, bookmark_dict):
                visited.append(value)
                if value == "Bookmarks Bar":
                    write_header(file, value)
                else:
                    write_folder(file, value)
                counter_current += parse_values(bookmark_dict, bookmark_object, value, bookmark_dict[value], visited,
                                                counter_current,
                                                file)
                write_closing_group(file)
            else:
                visited.append(value)
                write_item(file, value, bookmark_object[value].get("url"))
    return counter_current - counter


def write_bookmark_elements(bookmark_dict, bookmark_object, file):
    visited = []
    parse_values(bookmark_dict, bookmark_object, "root", bookmark_dict["root"], visited, 0, file)


def write_bookmark_header(file):
    file.write("<!DOCTYPE NETSCAPE-Bookmark-file-1>\n")
    file.write("<!-- This is an automatically generated file.\n")
    file.write("     It will be read and overwritten.\n")
    file.write("     DO NOT EDIT! -->\n")
    file.write("<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\">\n")
    file.write("<TITLE>Bookmarks</TITLE>\n")
    file.write("<H1>Bookmarks</H1>\n")
    file.write("<DL><p>")
    file.write("\n\t")


def parse_bookmark_file(root, csv_file_name):
    """parse the bookmark csv to create bookmark structure in HTML"""
    with open(os.path.join(root, csv_file_name)) as csv_file:
        csvreader = csv.reader(csv_file, delimiter="\t")
        header_map = parse_header_data(next(csvreader))
        bookmark_dict, bookmark_object = process_csv_data(csv_file, header_map)
        with open("output/custom_bookmark.html", "w", encoding="utf8") as file:
            write_bookmark_header(file)
            write_bookmark_elements(bookmark_dict, bookmark_object, file)
            write_end_file(file)
        # write("output/custom_bookmark.html", bookmark_dict)


def loop_input_directory(input_dir):
    """loop the files within the input directory"""
    for (root, _, files) in os.walk(input_dir):
        for file in files:
            if 'bookmark.csv' in file:
                parse_bookmark_file(root, file)


if __name__ == '__main__':
    args = sys.argv
    loop_input_directory(args[1])
