import os, json


def find_file(file_name, path):
    list_files = os.listdir(path)
    for file in list_files:
        if file_name in file:
            return file    
    return ''


def load_json(path):
    json_file = open(path, encoding="utf8")
    json_content = json.load(json_file)
    json_file.close()
    return json_content
