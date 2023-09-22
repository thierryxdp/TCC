#Recebe uma lista e um número inteiro
#retorna uma lista com os mesmos numeros da lista anterior maior que o numero inserido
def maiores(lista:  list, n:int)->list:
    """Recebe uma lista e um número inteiro
	   retorna uma lista com os mesmos numeros 
	   da lista anterior maior que o numero inserido"""
    i=0
    tamanho=len(lista)
    lista2=[]
    while tamanho<=n:
        if lista[i] > n:
        	list.append(lista2,lista[i])
        	i=i+1
    return lista2