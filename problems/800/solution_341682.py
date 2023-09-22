#Funcao que recebe uma lista de compras e um dicionario contendo
#O preco de cada produto e retorna o valor total dos itens na lista
#disponíveis

def total(lista,itens_disponiveis):
    
    preco_final = 0
    for elem in lista:
        preco_final +=itens_disponiveis[elem]
    	
    round(preco_final, 2)
    return preco_final