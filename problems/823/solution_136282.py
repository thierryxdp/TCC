def faltante(lista):
    """
    	Função que dada uma lista com N-1 inteiros numericos
        de 1a N, descobre qual número deste intervalo está
        faltanto. 
        list -> int
    """
    i=1
    n = len(lista)
    while i<=n:
        if i not in lista:
            return i
        i= i + 1
    if i>len(lista):
        return len(lista)+1