def maiores(lista,n):
    maior=[]
    for item in lista:
        if item >n:
            maior.append(item)
    maior.sort()
    return maior