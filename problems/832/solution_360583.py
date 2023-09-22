def eh_quadrada(matriz):
        #Verifica se uma matriz é quadrada(sem nenhuma linha nem coluna)
        #entrada: matriz ; saida: True ou False (booleana)

    for i in range(0, len(matriz)):
        for o in range(0, len(matriz[i])):
            if len(matriz) == len(matriz[i]) and len(matriz[o]):
                return True

            else:
                return False

    return True