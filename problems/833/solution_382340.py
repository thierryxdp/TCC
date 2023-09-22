def conta_numero (numero,matriz):
    '''Função conta quantas vezes o 'numero' aparece na 'matriz'. 
    int, list -> int'''
        qtd = 0
        for i in range (len (matriz)):
            for j in range (len(matriz[i])):
                if matriz[i][j] == numero:
                    qtd = qtd +1 
        return qtd