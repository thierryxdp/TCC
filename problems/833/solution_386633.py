def conta_numero(numero,matriz):
    ''' dada um numero e uma matriz de entrada ira retorna a quantidade de vezes que esse numero esta presente na matriz.
    int, matris = int '''
    qtd = 0
    indice = 0
    for lista in matriz:
        if numero in matriz[indice]:
            qtd += list.count(matriz[indice],numero)
            indice += 1
        else :
            indice += 1
    return qtd