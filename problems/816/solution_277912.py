def maiores(numeros,n):
    list.append(numeros,n)
    list.sort(numeros)
    pos_n=list.index(numeros,n)
    list.pop (numeros,>=pos_n)
    return numeros