def filtraMultiplos(lista, numero):
    """função que recebe como entrada uma lista de números e um
    número n e retorna uma nova lista com os números divisiveis
    pelo número n informado.
    list, int -> list"""
    i = 0
    listaNova = []
    while i < len(lista):
        if lista[i] % numero == 0:
             listaNova = listaNova + [lista[i],]
        i = i + 1
    return listaNova