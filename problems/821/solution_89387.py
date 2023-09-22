def fatorial (numero):
    """retorna o fatorial do número de entrada; int -> int"""
    antecessor = 0
    fator_multiplicativo = 1
    while numero - antecessor > 1:
        fator_multiplicativo = (numero - antecessor)*fator_multiplicativo
        antecessor = antecessor + 1
    return fator_multiplicativo