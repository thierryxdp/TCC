def total (lista, dicionario):
    soma = 0
    chaves = list(dict.keys(dicionario))
    valores = list(dict.values(dicionario))
    for c in chaves:
        if lista[c] in chaves:
            soma = soma + valores[c]
    return soma
    
total (['biscoito'], {'biscoito':4.99})