"""Recebe uma lista de compras e um dict com os preços de 
cada produto e retorna a soma total dos itens disponíveis
na loja.
Assinatura: list dict --> float
Testes:
lista = ['pão','batata','arroz']
produtos = {'pão':2.99, 'batata':5.70, 'arroz':6.80}
total(lista, produtos)
15.49
"""
def total(lista,produtos):
    soma=[]
    for i in range(0,len(lista)):
        if lista[i] in produtos:
            soma.append(produtos[lista[i]])
        	i=i+1
    return round(sum(soma),2)