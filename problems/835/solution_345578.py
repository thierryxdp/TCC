# Função melhor volta

def melhor_volta(matriz):
        '''Dada uma matriz 6x10, com os tempos em segundos dos corredores a cada volta, retorna uma tupla informando: de quem foi a melgor volta, qual o tempo da melhor voltam, qual foi o número da melhor volta.
        list(list) -> tuple'''
        tempos = 0
        for i in range(6):
                tempos += matriz[i]
                melhor_tempo = min(tempos)
                for j in range(10):
                        if matriz[i][j] == melhor_tempo:
                                melhor_corredor = i
                                melhor_volta = j
        return (melhor_corredor, melhor_tempo, melhor_volta)