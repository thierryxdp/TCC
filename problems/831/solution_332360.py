def lingua_p (palavra):
    '''função que recebe como parametro uma palavra em pot
    gues, e retorna essa palavra traduzida para lingua do P
    str->str'''
    resp=''
    indice=0
    for i in palavra:
        if palavra[indice] in 'aeiouAEIOU':
            resp+=str.replace(palavra,palavra[indice],(palavra[indice]+'p'))
    	indice+=1
    return resp