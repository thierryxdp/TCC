def maiores(lista,n):
    """funcao que dado uma lista de numeros int e um numero int n, retorna
    outra lista que contenha todos os numeros da lista original, mas sendo
    maiores que numero n. list,int->list"""
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind= list.index(lista,n)
    lista1= lista[ind+1:]
    ret