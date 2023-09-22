def lingua_p (palavra):
    '''c'''
    resp=''
    indice=0
    for i in palavra:
        if palavra[indice] in 'aeiouAEIOU':
            resp+=str.replace(palavra,palavra[indice],(palavra[indice]+'p'))
    	indice+=1
    return resp