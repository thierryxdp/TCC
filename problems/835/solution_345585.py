# Função melhor volta

def melhor_volta(matriz):
        '''Dada uma matriz 6x10, com os tempos em segundos dos corredores a cada volta, retorna uma tupla informando: de quem foi a melgor volta, qual o tempo da melhor voltam, qual foi o número da melhor volta.
        list(list) -> tuple'''
        tempo = []
        for i in range(6):
            tempo += [matriz[0][i]]
            tempo_min = min(tempo[i])
            print(tempo_min)
            for j in range(10):
                print(matriz[0][i][j])
                if matriz[0][i][j] == tempo_min:
                    corredor = i
                    volta = j
        return (corredor, tempo_min, volta)