def melhor_volta(matriz):
    """Uma pista de Kart permite 10 voltas
para cada um dos 6 corredores. A função
deve retornar uma tupla informando:
De quem foi a melhor volta da prova,
com qual tempo e em que volta."""
    nlin = len(matriz) #qnt de linha
    listapiloto = [] #criando lista
    listatempo = []
    listavolta = []
    

    for i in range(nlin):
        
        ncol = len(matriz[i])#qnt de coluna
        lista = []#criando lista vazia
         
        for j in range(ncol):
            list.append(lista,matriz[i][j]) #colocando os tempos dentro de uma lista separada
            
        listatempo += [min(lista)] #criando lista com os menores tempos, acumulando seus valores
        listavolta += [list.index(lista,min(lista))+1]  #criando lista com das voltas com menores tempos
        

    listapiloto = list.index(listatempo,min(listatempo))+1 #posição do piloto de menor tempo dentro da lista de menores tempos
    volta = list.index(listatempo,min(listatempo))#indice da volta de menor tempo dentro da lista de menores tempos
    

    return [listapiloto] + [min(listatempo)] + [listavolta[volta]]