def maiores(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero,reverse=True)
    a=list.index(lista_numero,n)
    b=lista_numero[:a]
    list.sort(b)#list.sort()不能atribui（ex:c=list.sort(b))
    
    return b



def acima_da_media(lista_notas):
    
    tamanho=sum(lista_notas)
    media=int(tamanho/len(lista_notas))
    return maiores(lista_notas,media)