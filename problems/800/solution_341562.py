def total(lista,produtos):
    #Separando os produtos que te na loja em chaves
    loja_tem = dict.keys(produtos)
    #Lista com os valores que serão somados de acordo com os produtos da loja
    compras = []
    #Pegando cada item da lista
    for item in lista:
        if item in loja_tem:
            valor = (produtos[item])
            list.append(compras,valor)
        else:
            compras = compras
	return sum(compras)