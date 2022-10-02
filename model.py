import docx2txt
from docx import Document
import sys
import os
from pyresparser import ResumeParser
from tkinter.filedialog import Open
import nltk
nltk.download('stopwords')

def namee(filen):
     filled = f'D:/CV/cvparser/CVs/{filen}'
    # try:
    #     doc = Document()
    #     with open(filled, 'r') as file:
    #         doc.add_paragraph(file.read())
    #         doc.save("text.docx")
    #         data = ResumeParser('text.docx').get_extracted_data()

    # except:
     data = ResumeParser(filled).get_extracted_data()
     return data

 