def fatorial(numero):
    """Função que recebe um numero, retornando o fatorial dele mesmo
    entrada: int
    retorno: int"""
    i= 2
    num=1
    while i<= numero:
        num= num*i
        i= i +1
    return num