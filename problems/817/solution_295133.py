def maiores(lista_inteiros,n):
    if n not in lista_inteiros:
        lista_inteiros.append(n)
    lista_inteiros.sort()
    i=lista_inteiros.index(n)
    return lista_inteiros[i+1:]

def acima_da_media(notas):
    media=sum(notas)/len(notas)
    return maiores(notas,media)