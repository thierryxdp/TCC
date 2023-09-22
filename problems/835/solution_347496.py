def melhor_volta(matriz:list) -> tuple:
    '''Recebe uma lista com 60 tempos de voltas de 6 carros em uam competição
    e retorna uma tupla informando de quem foi, com qual, e em que volta obteve aquele tempo.'''
    menor_valor = 0
    todos_tempos = [] 
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            todos_tempos.append(matriz[i][j])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if min(todos_tempos) == matriz[i][j]:
                return (i+1, matriz[i][j], j+1)