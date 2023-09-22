def melhor_volta(matriz):
    """A funcao nos diz qual corredor obteve a melhor volta seguido de seu melhor tempo a volta em que se deu tal tempo.A entrada é
    uma matriz em que cada linha corresponde aos corredores, a matriz de entrada de ter 6 linhas e 10 colunas, os tempos 
    deles.list(matriz)->tuple."""
    lista = []
    lista_voltas = []
    for i in range(len(matriz)):
        minimo = min(matriz[i])
        voltas = matriz[i].index(minimo)
        list.append(lista,minimo)
        list.append(lista_voltas,voltas)
    a = lista.index(min(lista))    
    return a + 1,min(lista),lista_voltas[a]+1