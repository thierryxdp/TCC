def melhor_volta(matriz):
    '''    Dada uma matriz, retorna uma tupla com o nome
    de quem fez a melhor volta, o melhor tempo e
    em quaantas voltas isso aconteceu.
    assinatura: matriz ---> tupla'''
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)