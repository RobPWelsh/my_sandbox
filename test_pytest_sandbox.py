from pathlib import Path

# Create a reference text file in the cwd
with open('ref_text.txt', 'w') as ref_text:
    ref_text.write('This is the text to compare.')


# Create a comparison text file and compare to the reference file using the tmp_path fixture
def test_create_file(tmp_path):
    with open('ref_text.txt') as ref_text:
        content = ref_text.read()
    tmp_dir = tmp_path / 'sub'
    tmp_dir.mkdir()
    tmp_file = tmp_dir / 'cmp_text.txt'
    print(tmp_file)  # test_pytest_sandbox.py C:\Users\rob.welsh\AppData\Local\Temp\pytest-of-Rob.Welsh\pytest-7\test_create_file0\sub\cmp_text.txt
    with tmp_file.open(mode='w') as cmp_text:
        cmp_text.write('This is the text to compare.')
    assert tmp_file.read_text() == content

