def maiores(lista_num,n):
    'função que recebe uma lista e um número x e retorna lista com os números maiores que x. int int'
    r=[]
    i=0
    while i<len(lista_num):
        if lista_num[i]>n:
            r=r+[lista_num[i],]
        i=i+1
    list.sort(r)
    return r