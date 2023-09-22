def maiores(lista_numeros, n):
    '''
    	Recebe uma lista e retorna apenas os valores maiores que o números dado pelo usuário.
        Parâmetro 1: list
        Parâmetro 2: int
        Resultado: list
    '''
    nova_lista = filter(n, lista_numeros)
    return nova_lista