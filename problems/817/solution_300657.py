def acima_da_media(lista): 
    L=lista
    soma=sum(L)
    qnt=len(L)
    media=soma/qnt
    list.append(L,media)
    list.sort(L)
    indece=list.index(L,media)
    novo_indece=indece+1
    L=L[novo_indece:]
    return L