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
            list.append(lista,matriz[i][j]) #colocando os valores dentro de uma lista separada

        listatempo = list.append(listatempo,min(lista)) #criando lista com os menores tempos
        listapiloto = list.append(listapiloto,(list.index(lista,min(lista))+1)) #posição do piloto de menor tempo

    listavolta = list.index(listatempo,min(lista))+1 #qual volta teve o menor tempo

    return listapiloto + min(listatempo) + listavolta