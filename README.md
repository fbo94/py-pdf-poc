# py-pdf-poc

POC destiné à étudier la possibilité de fusionner des fichiers pdf et de convertir des pages en PDF en images
## Librairies utilisées
 - [pyPDF2](https://github.com/mstamy2/PyPDF2)
 - [pdf2image](https://pypi.org/project/pdf2image/)
## Merge des pdfs
On utilise la libraire pyPDF2 pour ce faire.
```
python merge_multiple_pdf.py --input chemin/fichier1.pdf,chemin/fichier2.pdf --output monchemin.pdf(optionnel)
```
Cette commande enregistre les fichiers dans le chemin du paramètre output si renseigné, sinon dans storage/merges
## Export pdf -> jpeg (pdf2image)
```
python pdf_export_image.py --input redis-cheatsheet-v1.pdf
```
Enregistre les pages du pdf en image individuelle dans le dossier storage/images

