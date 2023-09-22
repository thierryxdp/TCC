def maiores(lista_numero,n):
    """essa funçao recebe somente numeros inteiros, retornando os numeros da lista_numero maiores do que n"""
    a=lista_numero 
    list.insert(a,0,n)
    list.sort(a)
    x=list.index(a,n)
    return a[1+x:len(a)]