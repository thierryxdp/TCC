def total(lista,preco):
    """funcao que determina o valor da compra dos produtos presentes na lista"""
    valor=0
    for l in lista:
        for p in preco:
            if l==p:
                valor+=preco.get(p)
    return (round(valor,2))