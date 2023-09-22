from collections import Counter
def repetidos(lista):
	lista = [4, 2, 1, 6, 1, 4, 4]
	contador = Counter(lista)

	repetidos = [
    	item for item, quantidade in contador.items() 
     	   if quantidade > 1
	]

	quantidade_repetidos = len(repetidos)
    return(quantidade_repetidos)