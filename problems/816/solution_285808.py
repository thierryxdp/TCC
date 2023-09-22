def maiores(lista_numeros, n):
    '''
    	Recebe uma lista e retorna apenas os valores maiores que o números dado pelo usuário.
        Parâmetro 1: list
        Parâmetro 2: int
        Resultado: list
    '''
    nova_lista = [x for x in lista_numeros if x > n]
    nova_lista.sort()
    return nova_lista