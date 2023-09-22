def fatorial(numero):
    """Função que, dado um numero, retorna seu valor fatorado"""
    i=1
    fatorial =1
    while i<=numero:
        fatorial*=i
        i=i+1
    return fatorial