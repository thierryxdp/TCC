#Start your python function here
def filtra_pares(a,b,c,d):
    """Função que recebe uma tupla com 4 elementos do tipo int, e retorna 
       uma nova tupla contendo apenas os elementos pares da tupla original,
       na mesma ordem que se encontravam.
       
       Parameters:
       a: Primeiro elemento da tupla
       b: Segundo elemento da tupla
       c: Terceiro elemento da tupla
       d: Último elemento da tupla
       
       tuple -> tuple
       """
    if a%2 == 0:
        return int(a)
    elif a%2==0 and b%2==0:
        return int(a,b)
    elif a%2==0 and b%2==0 and c%2==0:
        return int(a,b,c)
    elif a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return int(a,b,c,d)
    elif b%2==0:
        return int(b)
    elif b%2==0 and c%2==0:
        return int(b,c)
    elif b%2==0 and c%2==0 and d%2==0:
        return int(b,c,d)
    elif c%2==0:
        return int(c)
    elif c%2==0 and d%2==0:
        return int(c,d)
    elif d%2==0:
        return int(d)
    else:
        return ()