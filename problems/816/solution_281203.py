def maiores(lista,n):
    '''retorna os numeros da lista maiores que n; list,int->list'''
    maiores=[]
    if lista[0]>n:
        maiores=lista[0]
    if lista[1]>n:
        maiores=maiores+lista[1]
    if lista[2]>n:
        maiores=maiores+lista[2]
        
    return maiores