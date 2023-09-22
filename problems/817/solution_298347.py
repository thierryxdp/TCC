def maiores(lista,n):
    x = ([i for i in lista if i > n])
    return sorted(x)
def acima_da_media(listatodos):
    a = sum(listatodos)
    b = len(listatodos)
    c = a/b
    return maiores(listatodos,c)