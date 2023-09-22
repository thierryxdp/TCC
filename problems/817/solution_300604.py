def acima_da_media(lista): 
    L=lista
    soma=sum(L)
    qnt=len(L)
    y=soma/qnt
    n='%.0f'%y
    list.append(L,n)
    list.sort(L)
    indece=list.index(L,n)
    novo_indece=indece+1
    L=L[novo_indece:]
    return L