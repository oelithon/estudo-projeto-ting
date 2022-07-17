from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    path_list = list()
    len_instance = len(instance)

    for item in range(0, len_instance):
        path_list.append(instance.search(item))

    if path_file not in path_list:
        file_content = txt_importer(path_file)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content
        }
        instance.enqueue(path_file)

        return print(str(result), file=sys.stdout)


def remove(instance):
    if not len(instance):
        return print("Não há elementos", file=sys.stdout)
    
    removing_file = instance.dequeue()
    print(f'Arquivo {removing_file} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        search_file = instance.search(position)
        file_content = txt_importer(search_file)
        result = {
            "nome_do_arquivo": search_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content
        }
        print(result, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
