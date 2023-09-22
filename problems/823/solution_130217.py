def faltante(l):
    """
    Função que dada uma lista com N-1 inteiros, descubra qual número inteiro deste intervalo está faltando
    list -> int
    """
    num = len(l) + 1
    listaToda = range (1, num+1)
    i = 0
    
    while i < len(listaToda):
        if listaToda[i] not in l:
            return listaToda[i]
        i += 1