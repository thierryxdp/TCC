def fatorial(numero):
    """Função que dado um número retorna o fatorial
       desse número.
       int->int"""
    resultado=1
    count=1
    while count <= numero:
        resultado *= count
        count += 1
    return resultado