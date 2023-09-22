def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 com os tempos de cada corredor e
    retorna uma tupla informando de quem foi 
    a melhor volta e qual foi esse tempo;
    list -> tuple'''
    tempos=[]
    voltas=[]
    i=0
    for m in matriz:
        list.append(tempos,min(m))
        list.append(voltas,(list.index(m,min(m))
    return ((list.index(tempos,min(tempos))+1),min(tempos),(voltas[list.index(tempos,min(tempos))]+1)