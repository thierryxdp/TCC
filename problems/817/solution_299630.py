def acima_da_media(lista_notas):
    list.sort(lista_notas,reverse=True)
    tamanho=len(lista_notas)
    if (tamanho%2==0):
        meio=int(tamanho/2)
        novo=lista_notas[:meio]
        list.sort(novo)
        
        return novo
    else:
        meio1=int((tamanho-1)/2)
        novo1=lista_notas[:meio1]
        list.sort(novo1)
        return novo1