def lingua_p(palavra):   
    indece=1
    L=''
    while indece<len(palavra):
        if palavra[indece-1:indece] in 'aeiou':
            L+=palavra[indece-1:indece]+'p'+palavra[indece-1:indece]
        else:
            L+=palavra[indece-1:indece]
        indece=indece+1
    return L