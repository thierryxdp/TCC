def maiores(t,n):
    """retorna uma função que ao dicionar um número n a uma lista t,retorna uma nova lista
    com todos os numeros originais maiores que n. list,int -> list"""
    list.append(t,n)
    list.sort(t)
    maiores = []
    proximo = 0
    while proximo <len(t):
        if t[proximo] > n:
            list.append(maiores,t[proximo])
        proximo = proximo + 1
    return maiores