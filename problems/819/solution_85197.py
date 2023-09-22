def filtraMultiplos (listaNum,num):
	"""Calcula e retorna os numeros de uma lista(listaNum)
    que sao multiplos de um dado numero(num);
    list,int-->list"""
    i=0
    lista=[]
    while i<len(listaNum):
		if listaNum[i]%num==0:
			lista=lista+[listaNum[i]]
    	i=i+1
	return lista