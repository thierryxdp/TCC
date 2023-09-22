def melhor_volta(matriz):
    '''Função que recebe como entrada uma matriz de 6 linhas e 10 colunas com os tempos em segundos dos corredores em cada volta, a função retorna uma tupla contendo o corredor com o melhor tempo, o tempo dele e a volta na qual ele fez esse tempo.
       parâmetro de entrada:list
       valor de retorno:tuple'''
    minimos = []
    for i in range(len(matriz)):
        minimos += [min(matriz[i])]
    competidor =list.index(minimos,min(minimos))
    voltas = list.index(matriz[competidor],min(minimos))
    return (competidor+1,min(minimos),voltas+1)