def conta_numero(numero, matriz):
    '''função que verifica e retorna quantas vezes um número de entrada aparece em uma matriz também de entrada; int, list(lists) -> int'''
    
    aparicoes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                aparicoes = aparicoes+1
                
    return aparicoes