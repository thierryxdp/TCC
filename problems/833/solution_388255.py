def conta_numero (numero, matriz):
    '''Função que conta e retorna quantas vezes o número inteiro 
    aparece na matriz de tamanho qualquer.
    int, lista(lista) -> int'''
    contador= 0
    for ind_linha in range(len(matriz)):
        for ind_coluna in rangelen((matriz[ind_linha])):
            if ind_linha==numero and [ind_coluna]==numero:
                contador+= 1
            return contador