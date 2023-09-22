def fatorial(numero):
    
    """Essa funcao retorna o fatorial de um numero dado como entrada;
    int -> int """

    i = 1
    fatorial = 1
    
    while i <= numero:
        fatorial = fatorial * i
        i = i + 1
    return fatorial