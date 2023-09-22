def maiores(lista,n):
    '''retorna uma lista que contenha todos os numeros da lista original maiores que n, list,int->list'''
    lista1=[]
    for num in lista:
        if n<num:
            return lista1.append(num)