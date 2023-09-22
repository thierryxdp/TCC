from collections import Counter
def repetidos(lista):
	contador = Counter(lista)

	repetidos = [
    	item for item, quantidade in contador.items() 
     	   if quantidade > 1
	]

	quantidade_repetidos = len(repetidos)
    return(quantidade_repetidos)