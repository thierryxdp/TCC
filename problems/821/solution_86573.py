def fatorial (x):
    """Função que recebe como entrada um número x e deve retornar
    o seu fatorial.
    int-> int
    """ 

    fatorial=1
    i=2
    while x>=i:
        fatorial= fatorial * i
        i= i + 1

    return fatorial