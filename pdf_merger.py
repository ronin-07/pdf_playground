# pdf merger program

# add PyPDF2 module and run program from terminal

# give file names in order you want to merge after execution statement

import sys

import PyPDF2

inputs = sys.argv[1:]

out_file = input('Enter merged pdf name with extension:')


def combiner(lists):
    merger = PyPDF2.PdfFileMerger()
    for pdf in lists:
        merger.append(pdf)
    merger.write(f'{out_file}')


combiner(inputs)
