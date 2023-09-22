def faltante(lista):
    pecas= len(lista)+1
    lista.sort()
    i=1
    while i < pecas:
        if listta[i] != i:
            return i
        else:
            i += 1