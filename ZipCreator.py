import zipfile
import pathlib
#Using the zipfile import
def archive(filepaths, des_dir):
    des_path = pathlib.Path(des_dir,"compressed.zip")
    with zipfile.ZipFile(des_path, 'w') as archive:# creating a zipfile
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


import zipfile
import pathlib


