def faltante(lista):
    lista.sort()
    pecas = len(lista)+1
    for i in lista.reverse():
        if i != pecas:
            return i+1