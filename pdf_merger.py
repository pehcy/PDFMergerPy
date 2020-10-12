import tkinter as tk
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

merger = PdfFileMerger()

files = ["dumm2.pdf", "sign2_zy.pdf"]

# append file
for filename in files:
    merger.append(PdfFileReader(open(filename, "rb")))

merger.write("zy_private.pdf")
window = tk.Tk()
window.mainloop()

