def melhor_volta(matriz):
    """analisa o tempo de cada corredor de Kart em 10 voltas e
    retorna uma tupla com quem teve a melhor volta, seu respectivo tempo e 
    em que volta"""
    minimos=[]
    for linha in matriz:
        minimos=minimos+[min(linha)]
    menor_tempo=min(minimos)
    corredor=list.index(minimos,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    
    return (corredor+1,menor_tempo,volta+1)