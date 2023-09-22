def localizaCelulaComMenorValor(matriz):
    """ Retorna qual o piloto com a melhor volta, o melhor tempo, e em qual volta; list -> tupla """
    resp = [0,0];
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < matriz[resp[0]][resp[1]]:
                tempo = matriz[i][j];
                piloto=i+1;
                volta=j+1         
    return piloto,tempo,volta