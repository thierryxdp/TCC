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

def acima_da_media(notas, media = 5):
    '''
    	Recebe uma lista de notas e retorna uma lista apenas com as notas maiores que a média, que por padrão é 5.
        Parêmatro 1: list
        Parâmetro 2: int
        Resultado: list
    '''
    notas_acima_da_media = maiores (notas, media)
    return notas_acima_da_media