import tkinter as tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path

merger = PdfFileMerger()

queue = []

def open_file():
    filepath = askopenfilename(
        filetypes=[("PDF Files","*.pdf"), ("All Files", "*.*")]
    )
    if not filepath or Path(filepath).exists():
        return
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
    window.title("PDFMerger Tk")
    window.geometry("500x500")
    # not allowed resizing x y direction
    window.resizable(0,0)
    # frame = tk.Frame(master=window, width=600, height=420)
    # frame.pack()
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    
    fr_bg = tk.Frame(window, bd=10)
    btn_open = tk.Button(fr_bg, text="Open File(s)",
                command=open_file)
    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    fr_bg.pack()

    label_select = tk.Label(text="Select your files to be merge (in PDF format)")
    label_select.pack()
    
    framed_btn = tk.Frame(window, relief=tk.RAISED, bd=2)
    
    # Button to merge pdfs
    btn_merge = tk.Button(master=window,text="Merge PDF", command=merge_pdfs)
    btn_merge.pack()

    btn_append = tk.Button()

    window.mainloop()
