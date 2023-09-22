def filtraMultiplos (lista_numeros, n):
    '''
    	Recebe uma lista de números e um número retornando uma lista contendo apenas os  numeros que são divisiveis por n.
        Parâmetro 1: list
        Parâmetro 2: int
        Resultado: list
 	'''
    numeros_divisiveis = []
    qtd_numeros = len(lista_numeros)
    count = 0
    while count != qtd_numeros:
        if lista_numeros[count] % n == 0:
            numeros_divisiveis.append(lista_numneros[count])
        count = count + 1
    return numeros_divisiveis