def total(l,d):
    """Dada uma lista de compras 'l' e um dicionário 'd' 
    contendo os produtos como chaves e os preços como valores
    de retorno, calcula o quanto a pessoa vai gastar"""
    a = []
    for e in l:
        a.append(d[e])
    return round(sum(a),2)