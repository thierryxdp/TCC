def soma(l):
    n = max(l)
    return int( (n+1)*n/2 )

def faltante(l):
    s = soma(l) - sum(l))
    return(s,len(l)+1)[s==0]