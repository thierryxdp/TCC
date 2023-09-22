def fatorial(numero):
    """Função que calcula o fatorial do numero de entrada fornecido
       int -> int"""
    resultado = 1
    conta = 1
    while conta <= numero:
        resultado = resultado*conta
        conta = conta + 1
    return resultado