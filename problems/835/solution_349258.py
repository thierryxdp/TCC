def melhor_volta(matriz):
    '''
    Recebe como entrada uma matriz 6x10 e retorna 
    uma tupla contendo: o corredor com a melhor volta,
    qual tempo e em que volta.
    
    list(list) -> tuple(int)
    pegar cada linha
    	verificar qual o menor tempo e qual o índice dele
    	adicionar a informação a uma lista
    pegar a lista e ver qual o menor tempo de todos
    pegar o índice
    retornar índice, tempo, índice
    '''
    lista = []
    for i in matriz:
        tempo = min(i)
        volta = i.index(tempo)
        lista.append([tempo,volta])
    for i[0] in lista:
        menor = min(i[0])
        corredor = list.index(menor)
        volta2 = corredor[1]
    return (corredor, menor, volta2)