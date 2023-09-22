def filtraMultiplos(t,n):
    ''''Função que recebe uma lista e um  numero e retorna  os multiplos do numero  lista-->lista  '''
    pares=[]
    proximo=0
    while proximo < len(t):
        
        if t[proximo]%n==0:
            pares=pares +[t[proximo]]
        proximo=proximo+1
    return pares