def total(lista,produtos):
    #Separando os produtos que te na loja em chaves
    loja_tem = dict.keys(produtos)
    #Lista com os valores que serão somados de acordo com os produtos da loja
    compras = []
    #Pegando cada item da lista
    for item in lista:
        if item in loja_tem:
            #Pegando os valores dos produtos que estão na lista
            # e tem na loja e incluindo na lista compras
            valor = (produtos[item])
            list.append(compras,valor)
        #Para o caso de produtos que estão na lista mas não tem
        # na loja
        else:
            compras = compras
	return round(sum(compras),2)