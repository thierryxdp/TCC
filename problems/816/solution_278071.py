def maiores(lista_inteiros,n):
    if n in lista_inteiros:
        indice=lista_inteiros.index(n)
        nova_lista=lista_inteiros[:]
    if n not in lista_inteiros:
        nova_lista=lista_inteiros
        lista_inteiros.append(n)
        lista_inteiros.sort()
        indice=lista_inteiros.index(n)
    return nova_lista[indice+1:]