def total(lista,preco):
    '''funcao que dado uam lista de compras e um dicionario com o preço de cada produto disponivel,retorne o valor total dos itens da lista que estejam disponiveis na loja; lista,dicionario -> float'''
    pagamento = 0
    for produtos in lista:
        pagamento = pagamento + dict.get(preco,lista)
    return round(pagamento,2)