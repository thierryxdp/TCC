def total(x,y):
    'dado um dicionario contendo os valores dos produtos e uma lista de compras, calcula o custo para faze-las list, dict -> float'
    x = [chocolate, maca, laranja]
    y = {chocolate, maca, laranja, pera, uva}
    itens = len(x)
    k=0
    soma = []
    while (k<itens):
        soma = soma + list(y[x[k]])
        k = k+1
    return soma