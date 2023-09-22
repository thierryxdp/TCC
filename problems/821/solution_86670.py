def fatorial(numero):
    """Função que recebe um numero e calcula o fatorial deste numero.
    int --> int"""
    i=1
    fatorial=1
    while i<=numero:
        fatorial= fatorial*i
        i+=1
    return fatorial