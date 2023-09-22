def colchao(dimensoes,h,l):
    """

    """
    if dimensoes[0]<=h:
        dim1=True
        if dimensoes[1]<=l or dimensoes[2]<=l:
            dim2=True
            if dim1 and dim2 == True:
                return True
    else:
        return False 
    if dimensoes[1]<=h:
        dim3=True
        if dimensoes[0]<=l or dimensoes[2]<=l:
            dim4=True
            if dim3 and dim4 ==True:
                return True
    else:
        return False
    if dimensoes[2]<=h:
        dim5=True
        if dimensoes[0]<=l or dimensoes[1]<=l:
            dim6=True
            if dim5 and dim6 == True:
                return True
    else:
        return False