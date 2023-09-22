def repetidos(lista):

	total = len(lista)
    d1 = 0
    d2 = 1
    qtd_vezes = 0
    
    while d2 != total:
        
		if lista[d1] == lista[d2]:
            qtd_vezes += 1
            d1 += 1
            d1 += 1
            
		else:
            d1 += 1
            d2 += 1
            
	return qtd_vezes