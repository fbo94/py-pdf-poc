# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pdf2image import convert_from_path
from datetime import datetime
import sys
import getopt
import os


def pdf_export_image(pdf_file, output_filename):
    if output_filename is None:
        output_filename = datetime.now().strftime("%d%m%Y%H%M%S") + '.pdf'

    images = convert_from_path(pdf_file)
    save_path = 'storage/images/' + output_filename.replace("pdf", "")
    os.mkdir(save_path)
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(save_path + '/'+output_filename + '_' + str(i) + '.jpg', 'JPEG')


def main(argv):
    inputfile = None
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
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
    if inputfile is not None:
        print('Conversion du pdf en image du fichier : ', inputfile)
        pdf_export_image(inputfile, outputfile)
    else:
        print('Aucun fichier pour la conversion du pdf en image')


if __name__ == "__main__":
    main(sys.argv[1:])


