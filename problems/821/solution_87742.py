def fatorial(numero):
    """Função que retorna a fatorial do numero dado.
    int - > int"""
    i=1
    fatorial =1
    
    while i<=numero:
        fatorial=fatorial*i
        i=i+1
    return fatorial