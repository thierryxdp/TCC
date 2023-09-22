def total(listaDeCompras,dicionario):
    x=0
    for i in dicionario:
        if i==listaDeCompras:
            x=round((x+dicionario[i]),2)
    	return x