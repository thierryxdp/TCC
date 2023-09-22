#Questão2
def total(lista,dicionario):
    '''Função que retorna a conta do supermercado da compra de cada item da lista de compras'''
    sigma = 0 
    for coisa in lista:
        if coisa in dicionario:
            sigma += dicionario[coisa]
    return round(sigma,2)