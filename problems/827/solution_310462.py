def qtd_divisores (n):
    """Funcao que conta a quantidade de divisores de um inteiro n"""
    ls = []
    for c in range (1, n+1):
        if n % c == 0:
            ls.append (c)
   return len(ls)