from tkinter import filedialog as fd
from PIL import Image
import os

files_to_edit = fd.askopenfilenames()
for file_name in files_to_edit:
    img = Image.open(file_name)
    img.save(file_name+".png")
    os.remove(file_name)

