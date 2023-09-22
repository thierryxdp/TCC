def total(x,y):
    'dado um dicionario contendo os valores dos produtos e uma lista de compras, calcula o custo para faze-las list, dict -> float'
    itens = len(x)
    k=0
    soma = []
    while (k<itens):
        l=list(y[x[k]])
        soma = soma + l
        k = k+1
    return sum(soma)