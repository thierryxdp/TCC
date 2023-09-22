def lingua_p (palavra):
    '''c'''
    resp=''
    indice=0
    for i in palavra:
        if palavra[0] in 'aeiouAEIOU':
            resp+=palavra[0]+str('p')+str.replace(palavra,palavra[0],'')
            break
    	indice+=1
    return resp