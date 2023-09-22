def soma(l):
    return (max(l)**2+x)/2

def faltante(l):
    somatorio = int(soma(l) - sum(l))
    return(somatorio,len(l)+1)[somatorio==0]