def maiores(lista,n):
    '''retorna os numeros da lista maiores que n; list,int->list'''
    maior=[]
    if lista[0]>n and len(lista)>=1:
        maior=lista[0]
    if lista[1]>n and len(lista)>=2:
        maior=maior+[lista[1]]
    if lista[2]>n and len(lista)>=3:
        maior=maior+[lista[2]]
    if lista[3]>n and len(lista)>=4:
        maior=maior+[lista[3]]
    if lista[4]>n and len(lista)>=5:
        maior=maior+[lista[4]]
    if lista[5]>n and len(lista)>=6:
        maior=maior+[lista[5]]
    if lista[6]>n and len(lista)>=7:
        maior=maior+[lista[6]]
    if lista[7]>n and len(lista)>=8:
        maior=maior+[lista[7]]
    if lista[8]>n and len(lista)>=9:
        maior=maior+[lista[8]]
    list.sort(maior)
    return maior