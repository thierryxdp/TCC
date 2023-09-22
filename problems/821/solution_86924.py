def fatorial (numero):
    '''Retorna o fatorial do número fornecido.
    int -> int'''
    resultado = 1
    contador = 1
    while contador <= numero:
        resultado = resultado * contador
        contador = contador + 1
    return resultado