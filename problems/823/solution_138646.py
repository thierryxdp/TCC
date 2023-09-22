def soma(l):
    s = max(l) + 1
    n = max(l)
    return s*n/2

def faltante(l):
    somatorio = int(soma(l) - sum(l))
    return(somatorio,len(l)+1)[somatorio==0]