def lingua_p(palavra):   
    indece=1
    L=''
    while indece<len(palavra)+1:
        if palavra[indece-1:indece] in 'AaáEeéIiíOoUuú':
            L+=palavra[indece-1:indece]+'p'+palavra[indece-1:indece]
        else:
            L+=palavra[indece-1:indece]
        indece=indece+1
    return str.lower(L)