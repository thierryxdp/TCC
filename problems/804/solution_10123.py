def filtra_pares(a,b,c,d):
    '''Funçao que apenas retorna os numeros pares 
    presentes no conjunto inicial
    int,int,int,int -> tuple'''
    pares=()
    if a%2==0:
        pares.append(a)
    elif b%2==0:
        pares.append(b)
    elif c%2==0:
        pares.append(c)
    elif d%2==0:
        pares.append(d)  
        return pares