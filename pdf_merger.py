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

if __name__ == "__main__":
    # create desktop GUI
    window = tk.Tk()
    window.title("PDF Merger Tk")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)
    
    framed_btn = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_merge = tk.Button(master=window,text="Merge PDF", command=merge_pdfs)
    btn_append = tk.Button()
    window.mainloop()
