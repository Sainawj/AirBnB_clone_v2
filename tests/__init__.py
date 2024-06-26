#!/usr/bin/python3
"""Module for testing the AirBnb clone modules.
"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """Clear the contents of the given stream.

    Args:
        stream (TextIO): The stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate()


def delete_file(file_path: str):
    """Remove a file if it exists.

    Args:
        file_path (str): The path of the file to remove.
    """
    if os.path.exists(file_path) and os.path.isfile(file_path):
        os.remove(file_path)


def reset_store(store: FileStorage, file_path: str = 'file.json'):
    """Reset the items in the given store.

    Args:
        store (FileStorage): The FileStorage instance to reset.
        file_path (str): The path to the store's file. Defaults to 'file.json'.
    """
    with open(file_path, 'w') as file:
        file.write('{}')
    if store:
        store.reload()


def read_text_file(file_path: str) -> str:
    """Read the contents of a given file.

    Args:
        file_path (str): The path of the file to read.

    Returns:
        str: The contents of the file if it exists, otherwise an empty string.
    """
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return ''


def write_text_file(file_path: str, content: str):
    """Write text to a given file.

    Args:
        file_path (str): The path of the file to write to.
        content (str): The content to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(content)
