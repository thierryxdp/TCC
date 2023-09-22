def lingua_p(palavra):   
    indece=1
    L=''
    while indece<len(frase):
        if palavra[indece-1:indece] in 'aeiou':
            L+=palavra[indece-1:indece]+'p'
        else:
            L+=palavra[indece-1:indece]
        indece=indece+1
    return L