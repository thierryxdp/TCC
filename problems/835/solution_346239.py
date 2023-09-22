def melhor_volta(matriz):
    """Retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta;
       Entrada: list;
       Saida: tuple;
    """
    lista = []
    pessoa = 0
    volta = 0
    tempo = 100
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            if matriz[i][j] < tempo:
                tempo = matriz[i][j]
                pessoa = i + 1
                volta = j + 1
    return pessoa, tempo, volta