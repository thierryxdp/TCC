def maiores(l,n):
    """ Dada uma lista de numeros inteiros e um numero N, retorna outra lista,
   	que contenha todos os numeros da lista original maiores que n
    list,int>list"""
    
    if n in l:
        l.sort()
        i = list.index(l,n)
        return l[i+1:]
    else:
        l.append(n)
        l.sort()
        i = list.index(l,n)
        return l[i+1:]