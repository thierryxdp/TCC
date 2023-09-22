def maiores(lista,n):
    '''retorna uma nova lista com os numeros maiores que n em ordem crescente'''
    
    m = [x for x in lista if x > n]
    list.sort(m)

    return m

def acima_da_media(lista):
    '''retorna uma lista ordenada com as notas que ficaram acima da media'''
    '''list ->list'''
    list.sort(lista)
    a=sum(lista)
    b=len(lista)
    c=a//b
    d=maiores(lista,c)
    
    return lista[d+1:]