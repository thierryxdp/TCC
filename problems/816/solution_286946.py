def maiores(a,n):
    '''funçao que dada uma lista de tres numeros, e um outro numero,
    retorna outra lista que contem todos os numeros daa lista original
    maiores que n em ordem crescente'''
    '''list,int->list'''
    list.sort(a)
    lista=[]
    for i in a:
    	if i>n:
            lista.append(i)
    return lista