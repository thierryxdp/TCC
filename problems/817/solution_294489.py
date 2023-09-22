def acima_da_media(lista):
    """Retorna uma lista ordenada de forma crescente com as notas acima da média de acordo com as notas que são os elementos da lista que é o parâmetro;
    list->list"""
    a=sum(lista)/len(lista)
    b=lista+[a]
    b.sort()
    c=b.index(a)
    if a in lista:
        return b[c+2:]
    else:
        return b[c+1:]