def melhor_volta(w):
    '''funçao que recebe como uma entrada uma matriz e retorna uma tupla informando de quem foi
    a melhor volta da prova, com qual tempo e em que volta; 
    list->tuple'''
    tempo = []
    for l in w:
        tm = min(l)
    list.append(tempo,tm)
    x = min(tempo)
    cor = list.index(tempo,x) + 1
    for l in range(len(w)):
        for c in range(len(w[l])):
            if x == w[l][c]:
                v = c + 1
    return (cor,x,v)