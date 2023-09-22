def fatorial(numero):
    """Dado um número int retorna o fatorial desse número.""" 
    fat = 1
    indice = 1
    while indice <= numero:
        fat = fat*indice
        indice = indice + 1
    return fat