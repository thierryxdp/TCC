def conta_numero(numero,matriz):
    '''Funcao que pega o número de entrada e verifica quantas vezes ele aparece na matriz de entrada, retorna
    	quantas vezes ele aparece.
        int, int→int
        list,list→int'''
    contador= 0
    tamanho= len(matriz)
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if  matriz[linha][coluna] == numero:
                contador+= 1
    return contador