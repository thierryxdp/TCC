def insere(lista_numero, n):
    """fun ̧c~ao recebe uma lista de n ́umeros e um n ́umero,
    adiciona o n ́umero `a lista, a ordena e retorna lista.
    list, int--> list"""
    lista_numero.insert(0, n)
    list.sort(lista_numero)
    return lista_numero