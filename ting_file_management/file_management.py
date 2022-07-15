import readline
import sys

def txt_importer(path_file):
    file = list()

    if ".txt" not in path_file:
        return print("Formato inválido", file=sys.stderr)

    lines = open(path_file).readlines()

    for line in lines:
        line_break = line.split('\n')
        file.append(line_break[0])

    return file