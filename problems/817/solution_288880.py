def maiores(lista, n):
    """Função que dada uma lista de números e um inteiro 'n', retorna uma lista  com todos
    os números maiores que 'n';
    list, int -> list"""
    lista.append(n)
    lista.sort()
    p = lista.index(n)
    if n in lista:
        return lista[p+2:]
    else:
        return lista[p+1:]

def acima_da_media(lista):
    """Dada uma lista de notas retorna uma lista com apenas as notas acima da média;
    list -> list"""
    media = sum(lista)/len(lista)
    return maiores(lista, media)