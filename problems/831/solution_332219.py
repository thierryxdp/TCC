def lingua_p (palavra):
    '''c'''
    resp=''
    indice=0
    for i in palavra:
        if palavra[indice] in 'aeiouAEIOU':
            resp+=palavra[indice]+str('p')+str.replace(palavra,palavra[0],'')
            break
    	indice+=1
    return resp