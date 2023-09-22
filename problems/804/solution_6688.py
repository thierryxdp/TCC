def filtra_pares(a,b,c,d):
    """função que dados quatro elementos de uma tupla, retorne apenas os elementos pares da tupla original. entrada; int,int,int,int=> int"""
    par = (a,b,c,d[0]%2==0)
     if par:
        return 1 + pares(a,b,c,d[1:]) 
     else:
        return pares(a,b,c,d[1:])