def melhor_volta(m):
    """É dado como entrada uma matriz 6x10 em que as linhas 
    representam os 6 corredores e as colunas as 10 voltas em
    uma pista de Kart realizadas por eles. Retorna uma tupla
    contendo quem fez a melhor volta da prova, com qual tempo
    e em qual volta.
    lista(lista) -> tuple"""
    tempo = 1000
    for v in range(0, len(m)):
        for vt in range(0, len(m[v])):
            if min(m[v][vt], tempo) == m[v][vt]:
                tempo = min(m[v][vt], tempo)
                vencedor = v + 1
                volta = vt + 1
                
    return vencedor, tempo, volta