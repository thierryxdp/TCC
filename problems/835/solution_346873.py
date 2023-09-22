def melhor_volta(matriz):
    '''Funcao que recebe uma matriz 
    onde as linhas representam os corredores
    e as colunas os tempos que cada um fez 
    por volta, e retorna uma tupla que diz
    quem fez a melhor volta, com o melhor
    tempo e em qual volta.
    Dados de entrada: list[list] 
    Valor de saida: tuple
    '''
    menores_tempos = [] 
    for linha in matriz:
        menores_tempos.append(min(linha))
    menor_tempo = min(menores_tempos)
    corredor = list.index(menores_tempos,menor_tempo)
    volta = list.index(matriz[corredor], menor_tempo)
    return corredor+1, menor_tempo, volta+1