def maiores(l,n):
    #Retorna uma nova lista contendo todos os numeros da lista original maiores que n, list-->list
    l.append(n)
    lm=sorted(l)
    lm=l2[l2.index(n):]
    lm.remove(n)
    return lm