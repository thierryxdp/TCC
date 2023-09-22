def pares(a,b,c,d):
    """função que recebe 4 elementos de uma tupla e retorna
    uma nova tupla apenas com os elementos pares
    tupla -> tupla"""
    t=a,b,c,d
    subt=()
    if(a%2==0):
        subt=t[0]
    if(b%2==0):
        subt=subt,t[1]
    if(c%2==0):
        subt=subt,t[2]
    if(d%2==0):
        subt=subt,t[3]
    return subt