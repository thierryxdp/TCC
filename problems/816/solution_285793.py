def maiores(lista_numeros, n):
    '''
    	Recebe uma lista e retorna apenas os valores maiores que o números dado pelo usuário.
        Parâmetro 1: list
        Parâmetro 2: int
        Resultado: list
    '''
    x = n
    criterio = x > n
    nova_lista = filter(criterio, lista_numeros)
    return nova_lista