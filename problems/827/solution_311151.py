def qtd_divisores(numero):
    '''Recebe um número e retorna a quantidade de divisores que esse
    número tem (int -> int).'''
    contador = 0
    numeros = range(1, numero + 1)
    for n in numeros:
        if numero % n == 0:
            contador = contador + 1
    return contador