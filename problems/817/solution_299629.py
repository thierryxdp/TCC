def maiores(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero,reverse=True)
    a=list.index(lista_numero,n)
    b=lista_numero[:a]
    list.sort(b)
    
    return b

def acima_da_media(lista_notas):
    list.sort(lista_notas,reverse=True)
    tamanho=len(lista_notas)
    if (tamanho%2==0):
        meio=(tamanho/2)
        novo=lista_notas[:meio]
        list.sort(novo)
        return novo
    else:
        meio1=((tamanho-1)/2)
        novo1=lista_notas[:meio1]
        list.sort(novo1)
        return novo1