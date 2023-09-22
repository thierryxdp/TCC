def melhor_volta(matriz):
    '''Função que dado uma matriz com os dados dos corredores, retorna de quem foi a melhor volta, quanto tempo de corrida o corredor teve e em qual volta ele se destacou.
    list(list) -> tuple'''
    x = []
    for m in range(len(matriz)):
        x = x+[min(matriz[m])]
    tempo = min(x)
    corredor = list.index(x,tempo)
    volta = list.index(matriz[corredor],tempo)
    return (corredor + 1, tempo, volta + 1)