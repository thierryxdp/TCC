def total(lista):
    'função que recebe lista de compras e dicionário com preço dos produtos e'
    'retorna valor total dos ítens que tem, disponíveis'
    lista=[]
    preco=0
    n=0
    while n<len(lista):
        if lista[n] in produtos:
            preco=preco+dict.get(produtos,lista[n])
            n+=1
    return round(preco,2)