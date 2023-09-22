def maiores(lista,n):
    '''retorna os numeros da lista maiores que n; list,int->list'''
    maiores=[]
    len(lista)=a
    if lista[0]>n and a>=1:
        maiores=lista[0]
    if lista[1]>n and a>=2:
        maiores=maiores+[lista[1]]
    if lista[2]>n and a>=3:
        maiores=maiores+[lista[2]]
    if lista[3]>n and a>=4:
        maiores=maiores+[lista[3]]
    if lista[4]>n and a>=5:
        maiores=maiores+[lista[4]]
    if lista[5]>n and a>=6:
        maiores=maiores+[lista[5]]
    if lista[6]>n and a>=7:
        maiores=maiores+[lista[6]]
    if lista[7]>n and a>=8:
        maiores=maiores+[lista[7]]
    if lista[8]>n and a>=9:
        maiores=maiores+[lista[8]]
    list.sort(maiores)
    return maiores