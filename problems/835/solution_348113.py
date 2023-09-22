def melhor_volta(matriz):
    '''Função que receba como entrada uma matriz 6x10 e 
    	retorne uma tupla informando: de quem foi a melhor 
        volta, com qual tempo e em que volta. 
        list --> tupla.'''
    lista=[]
    for x in matriz:
        melhor_rodada=min(x)
        list.append(melhor_rodada,[])
        melhor_volta=min(lista)
        vencedor = lista.inde(melhor_volta)
        rodada = matriz[vencedor].index(melhor_volta)
    return vencedor + 1, melhor_volta, rodada + 1