def melhor_volta(matriz):
    '''função responsável por pegar uma matriz,matriz, que contenha os tempos de corredores em 10 voltas e retorne o corredor com o melhor tempo em sua respectiva volta'''
    tempo=[] 
    for i in matriz:
        tempo=tempo+[min(i)]
    ment=min(tempo)
    corredor=list.index(tempo,ment)
    volta=list.index(matriz[corredor],ment)
    return (corredor+1,ment,volta+1)