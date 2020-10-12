import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader

merger = PdfFileMerger()

queue = []

def open_file():
    filepath = askopenfilename(
        filetypes=[("PDF Files","*.pdf"), ("All Files", "*.*")]
    )
    with open (filepath, "r") as input_file:
        queue.append(filepath)

def merge_pdfs(files):
    for filename in files:
        merger.append(PdfFileReader(open(filename, "rb")))

def output_pdf(output_filename):
    merger.write(output_filename)

# window = tk.Tk()
# window.mainloop()

# print("Hello, world")

if __name__ == "__main__":
    window = tk.Tk()
    btn_merge = tk.Button(master=window,text="Merge PDF", command=merge_pdfs)
    window.mainloop()
