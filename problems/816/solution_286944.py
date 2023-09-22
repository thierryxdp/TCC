def maiores(lista,n):
    '''funçao que dada uma lista de tres numeros, e um outro numero,
    retorna outra lista que contem todos os numeros daa lista original
    maiores que n em ordem crescente'''
    '''list,int->list'''
    list.sort(lista)
    lista1=[]
    for i in lista:
    	if i>n:
            lista1.append(i)
    return lista