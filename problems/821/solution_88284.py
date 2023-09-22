def fatorial(numero):
    """ A função ao receber um número como entrada, deve
    retornar o fatorial deste número.
    Entrada: Int
    Saída: Int"""
    
    valores = list(range(1,numero+1))
    fatorial = numero*(numero-1)
    return fatorial