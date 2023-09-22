def maiores(lista_num, n):
    """retorna os numeros maiores que n em ordem. (list,int->list)"""
    lista_maiores = []
    x=0
	while x<len(lista_num):
    	if lista_num[x]>n:
    		list.append(lista_maiores,lista_num[x])
        	x=x+1
        else:
            x=x+1
    list.sort(lista_maiores)        
    return lista_maiores