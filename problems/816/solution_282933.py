def maiores(lista,n):
    '''retorna os numeros da lista maiores que n; list,int->list'''
    maiores=[]
    if lista[0]>n and len(lista)>=1:
        maiores=lista[0]
    if lista[1]>n and len(lista)>=2:
        maiores=maiores+[lista[1]]
    if lista[2]>n and len(lista)>=3:
        maiores=maiores+[lista[2]]
    if lista[3]>n and len(lista)>=4:
        maiores=maiores+[lista[3]]
    if lista[4]>n and len(lista)>=5:
        maiores=maiores+[lista[4]]
    if lista[5]>n and len(lista)>=6:
        maiores=maiores+[lista[5]]
    if lista[6]>n and len(lista)>=7:
        maiores=maiores+[lista[6]]
    if lista[7]>n and len(lista)>=8:
        maiores=maiores+[lista[7]]
    if lista[8]>n and len(lista)>=9:
        maiores=maiores+[lista[8]]
    list.sort(maiores)
    return maiores