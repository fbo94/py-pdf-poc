# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime
import sys
import getopt


def merge_multiple_pdf(pdf_files, output_filename):
    if output_filename is None:
        output_filename = datetime.now().strftime("%d%m%Y%H%M%S") + '.pdf'

    new_file = open('storage/merges/'+output_filename, 'wb')
    pdf_writer = PdfFileWriter()
    for pdf_filename in pdf_files:
        pdf_read = PdfFileReader(pdf_filename)
        for page_file in pdf_read.pages:
            pdf_writer.addPage(page_file)

    with new_file as fh:
        pdf_writer.write(fh)


def main(argv):
    inputfiles = None
    inputfiles_list = []
    outputfile = None
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfiles = arg
            inputfiles_list = inputfiles.split(',')
        elif opt in ("-o", "--output"):
            outputfile = arg
    if len(inputfiles_list) > 0:
        print('Fusion des fichiers : ', inputfiles)
        merge_multiple_pdf(inputfiles_list, outputfile)
    else:
        print('Aucun fichier inséré pour la fusion des PDF')


if __name__ == "__main__":
    main(sys.argv[1:])


