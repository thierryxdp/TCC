def lingua_p (palavra):
    '''c'''
    resp=''
    indice=0
    for i in palavra:
        if palavra[indice] in 'aeiouAEIOU':
            return palavra[indice]+str('p')