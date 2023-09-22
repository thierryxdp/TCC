def fatorial(numero):
    """ Dado um número, retorna a fatorial desse número, ao
    iterar uma quantidade de número vezes, e multiplicar o número
    em questão pela variável resultado, que armazena o fatorial do número,
    assim iterando de 1 até o número, e a cada iteração realizando a multiplicação,
    para ao final retornar a fatorial do número passado.
    int -> int
    """
    i = 1
    resultado = 1
    while i <= numero:
        resultado *= i
        i += 1
    return resultado