def melhor_volta(matriz):
    '''
Função que  receba como entrada uma matriz 6 × 10 com os tempos em segundos dos corredores
em cada volta e retorna uma tupla informando: De quem foi a melhor volta da prova,
com qual tempo e em que volta.

list--->tuple
    '''
    i=0
    melhor=()
    lista=[]
    for linha in matriz:
        qtd=0
        for x in linha:
            list.apppend(lista,x)
    tempo=min(lista)
    
    for linha in matriz:
        qtd=0
        i=i+1
        for x in linha:
            if x==tempo:
                corredor=i
                corrida=linha.index(x)+1
    melhor=(corredor, tempo,corrida)