import sys

def txt_importer(path_file):
    if ".txt" not in path_file:
        return print("Formato inválido", file=sys.stderr)
