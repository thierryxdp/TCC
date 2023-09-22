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

def acima_da_media(lista_num):
    'função que recebe lista de notas e retorna lista ordenada com valores acima da média. int int'
    n=sum(lista_num)/len(lista_num)
    maiores(lista_num,n)
    r=[]
    i=0
    while i<len(lista_num):
        if lista_num[i]>n:
            r=r+[lista_num[i],]
        i=i+1
    list.sort(r)
    return r