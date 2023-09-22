def filtraMultiplos(lista, num):
    '''Funcao que dada uma lista de numeros, irá retornar outra lista apenas com os multiplos do numero informado. list, int -> list'''
    i=0
    lista1=[]
    while i<len(lista):
        if lista[i]%num==0:
            lista1=lista1+[lista[i],]
            i=i+1
        else:
            i=i+1
	return lista1