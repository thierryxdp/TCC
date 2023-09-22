def maiores(listaNumeros, n):
    if n not in listaNumeros:
        listaNumeros.append(n)
        listaNumeros.sort()
        i = listaNumeros.index(n)
        sublista = listaNumeros[i+1:]
        rep = sublista.count(n)
        return sublista[rep:]
    
def acima_da_media (lista_notas):
    '''funçao que dada como entrada uma lista com notas de uma turma
       retorna uma nova lista contendo apenas as notas acima da media'''
    '''list->list'''
    medias = (sum(lista_notas)/len(lista_notas))
    return maiores(lista_notas, medias)