def total(l,dp):
    ''' recebe uma lista de compras e um dicionário contendo o preço 
    de cada produto disponível em uma determinada loja, e retorna o valor 
    total dos itens da lista que estejam disponíveis nesta loja'''
    i=0
    s=0
    while i < len(l):
        c=l[i]
        s= s + dp[c]
        i+=1
    return round(s,2)