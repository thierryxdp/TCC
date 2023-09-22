def conta_numero(numero,matriz):
    
    '''Fução que dada uma matriz e um número,
    conta as ocorrencias desse número nessa matriz.
    
    int,list->int
    '''
    vezes=0
    for x in range(len(matriz)):
      	vezes=matriz[x].count(numero)
    return vezes