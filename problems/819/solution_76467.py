def filtramultiplos(lista,n):
    '''funcao que retorna todos os numeros da lista que orem divisiveis por n
    int,int->int'''
    i=0
    lista2=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(lista2,lista[i])
            i=i+1
    return lista2