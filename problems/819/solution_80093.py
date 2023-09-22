def filtraMultiplos(lista, numero):
    listaNova = []
    proxnumero = 0
    while proxnumero<len(lista):
        if lista[proxnumero]%numero == 0:
            listaNova = listaNova + [lista[proxnumero],]
        proxnumero = proxnumero + 1
    return listaNova