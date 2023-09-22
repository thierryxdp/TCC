def total(lista):
 '''função que recebe uma lista de compras e um dicionario contendo o preço dos produtos
 disponíveis em uma determinada loja e retorna o valor 
 total dos itens da lista disponíveis na loja
 list,dict--->float ou int'''

	disponiveis=[]
	for produto in lista:
    	if dict.get(cardapio,produto,0)!=0:
       		list.append(disponiveis,dict.get,(cardapio,produto,0)
                   
    return round(sum(disponiveis),2)