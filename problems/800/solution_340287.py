def total(lista, dicionario):
    '''Função que recebe uma lista com vários itens, sendo relativa
    	à uma lista de compras e um dicionário, sendo relativo aos
        produtos que um mercado tem e seus preços. Retorna a soma 
        dos valores dos produtos que estão na lista de compras e
        estão disponíveis no mercado
        
        list, dict -> float'''
    chaves = list(dict.keys(dicionario))
    valor_total = 0
    for i in range(len(lista)):
        if lista[i] in chaves:
            valor_total = valor_total + dict.get(dicionario,lista[i])
    return round(valor_total, 2)