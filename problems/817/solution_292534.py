def maiores(lista, n):
    list(lista)
    lista.append(n)
    lista_nov = sorted(lista)
    indN = lista_nov.index(n)
    if n not in lista_nov:
        lista.append(n)

    return lista_nov[indN + 1:]

def acima_da_media(lista):
    
    media = sum(lista)/(1.0*len(lista))
    alunosaprovados = maiores(lista, media)
    return alunosaprovados