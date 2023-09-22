def filtraMultiplos(l,n):
    'verifica em ordem os elementos de entrada de uma lista l'
    'quais deles sao multiplos de um numero n, e os posiciona'
    'em uma lista m'
    proximo=0
    m=[]
    while proximo <len(l):
        if l[proximo]%n == 0:
            m=m + [l[proximo]]
        proximo=proximo + 1 
    return m