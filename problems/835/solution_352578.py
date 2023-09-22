def melhor_volta(matriz):
    '''essa função recebe uma matriz com resultados de uma corrida, e retorna o vencedor, o melhor tempo e em qual corrida foi o melhor tempo'''
    '''list -> tuple'''
    qtd_linhas = len(matriz)
    resultado = 10000
    coluna = 0
    for i in range(qtd_linhas):
        melhor_tempo = min(matriz[i])
        if resultado > melhor_tempo:
             resultado = melhor_tempo
             corredor = i
             coluna = matriz[i].index(melhor_tempo)     

    return corredor+1, resultado,coluna