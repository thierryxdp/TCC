def total(compras,d):
	"""calcula o valor total das compras
    list,dict->float"""
    
    valor = 0
    
    for item in compras:

        valor = valor+d[item]
    
    return round(valor,2)