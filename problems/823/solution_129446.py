def faltante(lista):
    '''dada um quebra cabeca enumerado, esta funcao retorna a peca faltante
    list -> int'''
    ordenada = lista[:]
    list.sort(ordenada)
    completa = []
    for i in range(len(ordenada) + 1):
        list.append(completa, i + 1)
    contador = 0
    while contador < len(completa):
        if contador < len(ordenada):
            if completa[contador] != ordenada[contador]:
                return completa[contador]
        else:
            return completa[contador]
        contador += 1