def total(lista,produtos):
    """Recebe uma lista de compras e um dicionário com os preços de cada produto
e retorna a soma total dos itens disponíveis na loja.
Assinatura: list, dict --> float
lista= ["biscoito", "chocolate", "farinha"]
produtos = {"amaciante" : 4.99, "arroz": 10.90, "biscoito": 1.69, "cafe" : 6.98, "chocolate": 3.79, "farinha": 2.99}
 total(lista,produtos) == 8.47
"""
    soma=[]
    for i in range(0,len(lista)):
        if lista[i] in produtos:
            soma.append(produtos[lista[i]])
        i=i+1
    return round(sum(soma),2)