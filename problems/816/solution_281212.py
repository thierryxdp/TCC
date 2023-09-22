def maiores(lista,n):
    '''retorna os numeros da lista maiores que n; list,int->list'''
    maiores=[]
    if lista[0]>n:
        maiores=[lista[0]]
    if lista[1]>n:
        maiores=maiores+[lista[1]]
    if lista[2]>n:
        maiores=maiores+[lista[2]]
    if lista[3]>n:
        maiores=maiores+[lista[3]]
    if lista[4]>n:
        maiores=maiores+[lista[4]]
    if lista[5]>n:
        maiores=maiores+[lista[5]]
    if lista[6]>n:
        maiores=maiores+[lista[6]]
    if lista[7]>n:
        maiores=maiores+[lista[7]]
    if lista[8]>n:
        maiores=maiores+[lista[8]]
    list.sort(maiores)
    return maiores