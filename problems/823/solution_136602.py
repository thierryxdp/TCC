def listinha(lista):
    final = max(lista)
    contador = 0
    lista_edit = [final]
    resposta = 0
    
    while contador<final:
    	lista_edit+= [final-1]
    	final -= 1
    	contador+= 1  
	return lista_edit


def faltante(lista):
    resposta = 0
    
    if sum(lista) == sum(listinha(lista)):
        resposta = max(lista)+1
    
    elif sum(lista) != sum(listinha(lista)):
        resposta = sum(listinha(lista)) - sum(lista)
        
    return resposta