def melhor_volta(matriz):
    """A funcao nos diz qual corredor obteve a melhor volta seguido de seu melhor tempo.A entrada é
    uma matriz em que cada linha corresponde aos corredores, a matriz de entrada de ter 6 linhas e 10 colunas, os tempos 
    deles.list(matriz)->tuple."""
    lista = []
    for i in range(len(matriz)):
        maximo = min(matriz[i])
        list.append(lista,maximo)
    return lista.index(min(lista))+1,min(lista)