def filtro(x,n):
    if (x>n):
        return x

def maiores(k,n):
    filtrados = sorted(list(filter(filtro,k)))
    
    return filtrados