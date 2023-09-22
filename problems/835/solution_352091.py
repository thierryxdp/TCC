def melhor_volta(matriz):
    '''
    '''
    contar = 0
    lista = []
    voltas = []
    volta = 0
    for linha in matriz:
        volta = (linha.index(min(linha))+1)
        lista += [min(linha), ]
        voltas += [[volta], ]
        contar += 1
    tempo = min(lista)
    
    
    return (lista.index(min(lista))+1, min(lista), voltas[lista.index(min(lista))])