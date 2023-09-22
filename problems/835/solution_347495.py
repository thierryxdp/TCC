def melhor_volta(matriz:list) -> tuple:
    ''''''
    menor_valor = 0
    todos_tempos = [] 
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            todos_tempos.append(matriz[i][j])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if min(todos_tempos) == matriz[i][j]:
                return (i+1, matriz[i][j], j+1)