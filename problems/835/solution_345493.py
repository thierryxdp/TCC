def melhor_volta(m):
    '''Função que dada uma matriz m com os tempos em segundo em cada volta de cada corredor, retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta
    list[list] -> tuple(int, float, int)'''
    corredor=0
    tempos=[]
    voltas=[]
    for i in m:
        tempos+=[min(i)]
        voltas+=[list.index(i,min(i))]
    corredor=list.index(tempos,min(tempos))+1
    voltas=voltas[list.index(tempos,min(tempos))]+1
    tempos=min(tempos)
    return corredor,tempos,voltas