def faltante(lista):
    i = 1
    tamanho = len(lista)
    while i < tamanho + 1:
        if not i in lista:
            return i