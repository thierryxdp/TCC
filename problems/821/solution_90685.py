def fatorial(numero):
    '''função que dado um número retorna o seu fatorial
    int -> int
    '''
    resultado = 1
    contador = 1
    while contador <= numero:
        resultado *= contador
        contador += 1
    return resultado