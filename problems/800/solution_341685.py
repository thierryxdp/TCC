#Funcao que recebe uma lista de compras e um dicionario contendo
#O preco de cada produto e retorna o valor total dos itens na lista
#disponíveis

def total(lista,itens_disponiveis):
    
    preco = 0
    for elem in lista:
        preco +=itens_disponiveis[elem]
    
    preco_final = round(preco,2)
    return preco_final