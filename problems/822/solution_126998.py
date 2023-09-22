def repetidos(lista):
    indece=1
    S=[]
    while indece<=len(lista):
        if lista[indece-1:indece]==lista[indece:indece+1]:
            list.append(S,lista[indece:indece+1])
        indece=indece+1
    return len(S)