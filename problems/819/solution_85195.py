def filtraMultiplos (listaNum,num):
	"""Calcula e retorna os numeros de uma lista(listaNum)
    que sao multiplos de um dado numero(num);
    list,int-->list"""
    i=0
    lista=[]
    while i<len(lista):
		if lista[i]%num==0:
			lista=list.append(lista,lista[i])
    	i=i+1
	return lista