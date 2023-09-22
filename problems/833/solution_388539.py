def conta_numero(num, matriz):
    """ dado uma matriz e um número inteiro, retorna quantidade d vezes ue esse numero aparece dento da matriz.
    entrada matriz, inteiro -> saida inteiro. """
    
    qtd_repeticoes = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matri[i][j] == num:
                qtd_repeticoes = qtd_repeticoes + 1
    return qtd_repeticoes