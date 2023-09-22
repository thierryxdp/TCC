def maiores(lista,n):
    if n not in lista:
        lista.append(n)
        lista.sort()
        l = lista.index(n)
        lista2 = lista[l+1:]
        rep = lista2.count(n)
        return lista2[rep:]
    
    
def acima_da_media(notas):
    media = sum(notas)
    return maiores(notas,media)