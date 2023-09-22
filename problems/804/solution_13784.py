def filtra_pares(a,b,c,d):
    """Funcao que recebe 4 elementos inteiros e retorna apenas os elementos pares:int,int,int,int=>tuple"""
    x=(a,b,c,d)
    if (x[0]%2)=0 and (x[1]%2)=0 and (x[2]%2)=0 and (x[3]%2)=0:
        return x