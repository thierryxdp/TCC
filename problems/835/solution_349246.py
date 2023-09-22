def melhor_volta(m):
    '''recebe uma matriz 6 x 10(m) com tempos em segundos de 6 corredores
    em cada volta(total de 10 voltas) e retorna uma tupla informando:
    De quem foi a melhor volta, com qual tempo e em que volta; list -> tuple'''
    contagem = 1
    lista = []
    total = 0
    for i in m:
        lista.append(min(i))
    primeiro = min(lista)
    for j in m:
        if primeiro in j:
            return contagem,primeiro,(j.index(primeiro) + 1)
        else:
            contagem = contagem + 1