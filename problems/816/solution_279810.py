def maiores(lista,n):
    '''funcao que retorna os numeros da lista maiores que n. list,int->list'''
    lista2=[]
    for i in range(0,len(lista)):
       if lista[i]>n:
           lista2.append(lista[i])
    lista2.sort()
    return lista2