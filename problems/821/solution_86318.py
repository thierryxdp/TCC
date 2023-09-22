def fatorial(n):
    """Função que recebe um número e calcula o fatorial dele."""
    """int-->int"""
    i=0
    resultado=1
    lista=list(range(1,n+1))
    while i<len(lista):
        resultado=resultado*lista[i]
        i=i+1
    return resultado