__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import zipfile
from typing import List
import shutil


cache_folder_path = 'cache' 


def clean_cache():
    if os.path.isdir(cache_folder_path):
        shutil.rmtree(cache_folder_path)
    os.mkdir(cache_folder_path)


def cache_zip(zip_path: str, cache_path: str):
    clean_cache()
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_path)


def cached_files() -> List[str]:
    return list(filter(
        lambda path: os.path.isfile(path), 
        iter(os.path.abspath(os.path.join(cache_folder_path, x))  
             for x in os.listdir(cache_folder_path))))


def find_password(paths: List[str]) -> str:
    password_clue = 'password'
    for path in paths:
        with open(path, 'r') as f:
            rows = f.readlines()
            for row in rows:
                if password_clue in row:
                    return row.strip('\n').split(': ')[1]


if __name__ == '__main__':
    cache_zip('data.zip', cache_folder_path)
    paths = cached_files()
    password = find_password(paths)
    print(f"found password: '{password}'")
