import sys


def txt_importer(path_file):
    file = list()

    if ".txt" not in path_file:
        return print("Formato inválido", file=sys.stderr)
    try:
        lines = open(path_file).readlines()
        for line in lines:
            line_break = line.split('\n')
            file.append(line_break[0])
    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    return file
