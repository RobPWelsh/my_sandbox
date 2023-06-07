from pathlib import Path
import pytest

# Create a reference text file in the cwd
with open('ref_text.txt', 'w') as ref_text:
    ref_text.write('This is the text to compare.')


# Fixture to read contents of reference text
@pytest.fixture()
def read_ref_contents():
    """Returns contents of ref_text.txt"""
    with open('ref_text.txt') as ref_text:
        return ref_text.read()


# Create a comparison text file and compare to the reference file using the tmp_path fixture
def test_create_file(tmp_path, read_ref_contents):
    tmp_dir = tmp_path / 'sub'
    tmp_dir.mkdir()
    tmp_file = tmp_dir / 'cmp_text.txt'
    print(tmp_file)  # test_pytest_sandbox.py C:\Users\rob.welsh\AppData\Local\Temp\pytest-of-Rob.Welsh\pytest-7\test_create_file0\sub\cmp_text.txt
    with tmp_file.open(mode='w') as cmp_text:
        cmp_text.write('This is the text to compare.')
    assert tmp_file.read_text() == read_ref_contents


# Create a comparison text file and compare to the reference file using the tmp_path_factor fixture
def test_create_file_factory(tmp_path_factory, read_ref_contents):
    tmp_dir_2 = tmp_path_factory.mktemp('sub_factory')
    tmp_file_2 = tmp_dir_2 / 'cmp_text_2.txt'
    print(tmp_file_2)
    with tmp_file_2.open(mode='w') as cmp_text_2:
        cmp_text_2.write('This is the text to compare.')
    assert tmp_file_2.read_text() == read_ref_contents

