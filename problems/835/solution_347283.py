def melhor_volta(matriz):
    '''Função que recebe como entrada uma matriz com os tempos em segundos dos corredores em cada volta,e retorna o melhor tempo;
    Entrada: list
    Saída: int '''
    corredores=[]
    voltas=[]
    tempos=[]
    for i in matriz:
        for j in i:
            list.append(tempos,j)
            list.append(voltas,list.index(i,j))
            list.append(corredores,list.index(matriz,i))
    melhor_tempo=min(tempos)
    index=list.index(tempos,min(tempos))
    melhor_corredor=corredores[list.index(tempos,min(tempos))]+1
    melhor_volta=voltas[list.index(tempos,min(tempos))]+1
    return melhor_corredor,melhor_tempo,melhor_volta