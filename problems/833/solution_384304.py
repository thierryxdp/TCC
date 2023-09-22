def conta_numero(numero,matriz):
    """ Essa função conta quantas vezes o numero 
    esta na matriz. matriz,int->int."""
    num_linhas_matriz,num_colunas_matriz = len(matriz),len(matriz[0])
    contador = 0
    for i in range(num_linhas_matriz):
        x = list.count(numero,matriz)
        contador = contador + x
    return contador