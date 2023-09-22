def maiores(lista,n):
    '''retorna os numeros da lista maiores que n; list,int->list'''
    maior=[]
    if len(lista)>=1 and lista[0]>n:
        maior=lista[0]
    if len(lista)>=2 and lista[1]>n:
        maior=maior+[lista[1]]
    if len(lista)>=3 and lista[2]>n:
        maior=maior+[lista[2]]
    if len(lista)>=4 and lista[3]>n:
        maior=maior+[lista[3]]
    if len(lista)>=5 and lista[4]>n:
        maior=maior+[lista[4]]
    if len(lista)>=6 and lista[5]>n:
        maior=maior+[lista[5]]
    if len(lista)>=7 and lista[6]>n:
        maior=maior+[lista[6]]
    if len(lista)>=8 and lista[7]>n: 
        maior=maior+[lista[7]]
    if len(lista)>=9 and lista[8]>n:
        maior=maior+[lista[8]]
    list.sort(maior)
    return maior