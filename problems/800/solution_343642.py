"""Recebe uma lista de compras e um dict com os preços de 
cada produto e retorna a soma total dos itens disponíveis
na loja.
Assinatura:
Testes:
"""
def total(lista,produtos):
    soma=[]
    for i in range(0,len(lista)):
        if lista[i] in produtos:
            soma.append(produtos[lista[i]])
        	i=i+1
    return round(sum(soma),2)