def fatorial(n):
    """Essa função calcula o fatorial do número dado no
    argumento. int->int."""
    contador = n
    while contador > 0:
        fatorial = n *(n-1) *(n-2) 
        novofatorial = fatorial 
        contador = contador -1 
    return novofatorial