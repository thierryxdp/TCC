def fatorial(n):
    """
   Retorna o fatorial de um número.
   int -> int
   """
    lista_n= list(range(n+1))
    list.remove(lista_n,0)
    fatorial=1
    indice=0
    while indice<len(lista_n):
        fatorial=fatorial*lista_n[indice]
        indice=indice+1
    return fatorial