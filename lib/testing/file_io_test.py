# test_file_io.py
import pytest
from file_io import write_file, append_file, read_file

def test_write_file(tmp_path):
    """Test write_file()"""
    file_path = tmp_path / "test_file.txt"
    file_content = "This is a test content."
    write_file(file_path, file_content)
    with open(file_path, 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content

def test_append_file(tmp_path):
    """Test append_file()"""
    file_path = tmp_path / "test_file.txt"
    file_content = "This is a test content."
    append_content = "\nAppended content."
    write_file(file_path, file_content)
    append_file(file_path, append_content)
    with open(file_path, 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content + append_content

def test_read_file(tmp_path):
    """Test read_file()"""
    file_path = tmp_path / "test_file.txt"
    file_content = "This is a test content."
    write_file(file_path, file_content)
    file_content_read = read_file(file_path)
    assert file_content_read == file_content
