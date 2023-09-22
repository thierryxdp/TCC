def melhor_volta(matriz):
        '''Dada uma matriz 6x10, com os tempos em segundos dos corredores a cada volta, retorna uma tupla informando: de quem foi a melgor volta, qual o tempo da melhor voltam, qual foi o número da melhor volta.
        list(list) -> tuple'''
        tempo = []
        for i in range(6):
            for j in range(10):
                tempo.append(matriz[0][i][j])
                tempo_min = min(tempo)
                if matriz[0][i][j] == tempo_min:
                    corredor = i+1
                    volta = j+1
        return (corredor, tempo_min, volta)