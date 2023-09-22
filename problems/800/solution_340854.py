def total(lista, dic):
    soma = 0
    for itens in lista:
        if itens in dict.keys(dic):
            valor = dict.values(dic) 
            soma += valor 
	return soma