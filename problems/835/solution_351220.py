def melhor_volta(m):
    '''recebe uma matriz 6x10 com os tempos dos corredores
    de kart por volta e retorna de quem foi a melhor volta,
    com qual tempo e em que volta
    list(list)->tuple'''
    tempos = []
    volta = []
    for i in range(len(m)):#i são os tempos(10ea) de cada corredor
        mm = min(m[i])
        list.append(tempos,mm)
        list.append(volta,list.index(m[i],mm))
        
    menor = min(tempos)
    return (list.index(tempos,menor),menor,list.index(volta,list.index(tempos,menor)))