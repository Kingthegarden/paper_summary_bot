import os
from urllib.parse import urlsplit
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.pdf import *
import json

def write_file(name: str, file: str):
    if not os.path.exists(name):
        with open(name, 'w') as f:
            f.write(file + '\n')
    else:
        with open(name, 'a') as f:
            f.write(file + '\n')
    f.close()


def is_valid_url(url):
    try:
        result = urlsplit(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def get_pdf_docs(text: str, is_local: bool):
    if is_local:
        loader = PyPDFLoader(text)
    else:
        loader = OnlinePDFLoader(text)
    documents = loader.load()
    
    return documents[0].page_content