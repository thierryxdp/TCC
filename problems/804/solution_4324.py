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
        return (a)
    elif a%2==0 and b%2==0:
        return (a,b)
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    elif a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    else:
        return ()