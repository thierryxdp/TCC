def fatorial(numero):
    """Função que dado um número retorna o fatorial
       desse número.
       int->int"""
    resultado=1
    i=1
    while i <= numero:
        resultado *= i
        i += 1
    return resultado