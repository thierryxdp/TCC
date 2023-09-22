def maiores(x,n):
    '''função que filtra uma lista de números e retorna
    outra lista com os numeros maiores de n em ordem
    crescente
    list>>list'''
    list.append(x,n)
    list.sort(x)
    z=len(x)
    y=list.index(x,n)
    return x[y+1:z]
def acima_da_media(lista):
    a=sum(lista)
    b=len(lista)
    c=a/b
    return maiores(lista,c)