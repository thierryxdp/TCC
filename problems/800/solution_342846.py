def total(listadecompras,diciodeprecos):
    """Recebe uma lista de compras e um dicionario contendo os valores de todos os itens em uma loja e devolve o valor que e necessario para se comprar toda a lista;
    	list, dict -> float"""
    valor=0
    for i in range(len(listadecompras)):
        if listadecompras[i] in diciodeprecos:
            valor=valor+ diciodeprecos[listadecompras[i]]
    return round(valor,2)