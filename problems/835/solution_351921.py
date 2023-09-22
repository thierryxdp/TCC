def melhor_volta(matriz):
    '''
Função que  receba como entrada uma matriz 6 × 10 com os tempos em segundos dos corredores
em cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
com qual tempo e em que volta.

list--->tuple
    '''
    melhor=()
    lista=[]
    i=0
    for linha in matriz:
        qtd=0
        for x in coluna:
            lista.apppend(x)
    tempo=min(lista)
    
    for coluna in matriz:
        qtd=0
        for x in coluna:
            if x==tempo:
                corredor=i
                corrida=coluna.index(x)+1
    melhor=(corredor, tempo,corrida)
    return melhor