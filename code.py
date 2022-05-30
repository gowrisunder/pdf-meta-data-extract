import pikepdf
import sys

name = sys.argv[1]

pdf = pikepdf.Pdf.open(name)
docinfo = pdf.docinfo
for key, value in docinfo.items():
    print(key, ":", value)

