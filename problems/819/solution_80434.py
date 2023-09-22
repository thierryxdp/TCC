def filtraMultiplos(lista,N):
'''dada uma lista de numeros inteiros e um numero N inteiro 
	essa funçao devolve os elementos da lista que sao multiplos 
	de N
	list,int-->int'''
    listaNumerosMultipolsN=[]
    a=0
    listaCopia=lista[:]
    while a<len(listaCopia):
        if lista[a]%N==0:
            listaNumerosMultipolsN=listaNumerosMultipolsN+[lista[a]]
        a=a+1
    return listaNumerosMultipolsN