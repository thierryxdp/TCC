def conta_numero(numero,matriz):
    '''
    	Função que diz quantos elementos 'numero' possui uma matriz de numeros inteiros.
        int,list -> int
    '''
    vezes_n = 0
    for i in range(len(matriz)):
        vezes_n +=list.count(matriz[i],numero)
    return vezes_n