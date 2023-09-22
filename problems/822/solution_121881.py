def repetidos(n,lista):
    if n in lista:
        repeticao=lista.count(n)
    	return "Este item se repete", repeticao, "vezes".
    else: 
        return "Este item nao esta na lista"