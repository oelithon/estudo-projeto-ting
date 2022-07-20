from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    result = list()
    len_instance = len(instance)
    for item in range(len_instance):
        frequency_word = list()
        search_file = instance.search(item)
        data = txt_importer(search_file)
        len_data = len(data)
        for line in range(len_data):
            if word.upper() in data[line].upper():
                frequency_word.append({"linha": line + 1})

        if frequency_word:
            result.append({
                "palavra": word,
                "arquivo": search_file,
                "ocorrencias": frequency_word,
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
