def qtd_divisores(t,n):
    ''' Função que  contas os divisores de um numero , int->int''''
    pares=[]
    proximo=10
    for proximo in len(t):
        
        if t[proximo]%n==0:
            pares=pares +[t[proximo]]
        proximo=proximo+1
    return n