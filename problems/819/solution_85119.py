def filtraMultiplos(lista,numero):
    """funcao"""
    listaF = []
    contador = 0
    numerodetermosdalista = len(lista)
    while contador < numerodetermosdalista:
        if (numero % lista[c]) == 0:
            resposta = listaF + [lista[c]]
            contador += 1
    	else:
        	contador += 1
	return resposta