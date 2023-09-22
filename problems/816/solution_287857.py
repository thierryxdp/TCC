def maiores(l,n):
    #Retorna uma nova lista contendo todos os numeros da lista original maiores que n, list-->list
    l.append(n)
    l2=sorted(l)
    l2=l2[l2.index(n):]
    l2.remove(n)
    return l2