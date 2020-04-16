# program to add any watermark in pdf

# add all files to project folder

import PyPDF2

# enter names with extensions

inp_file = input('Enter name of pdf:')
wtr_file = input('Enter name of pdf which has watermark:')
out_file = input('Enter name of output file:')

inp = PyPDF2.PdfFileReader(open(f'{inp_file}', 'rb'))
wtrmark = PyPDF2.PdfFileReader(open(f'{wtr_file}', 'rb'))
output = PyPDF2.PdfFileWriter()
for i in range(inp.getNumPages()):
    pdf_page = inp.getPage(i)
    page = wtrmark.getPage(0)
    pdf_page.mergePage(page)
    output.addPage(pdf_page)

output.write(open(f'{out_file}', 'wb'))
