def uppCons(frase):
    '''
        Dada uma frase a função retorna a frase com as suas
        consoantes em maiúsculo.
        str -> str
    '''
    i=0
    frase_upp=[]
    while i<len(frase):
        if str.lower(frase[i]) in 'bcçdfghjklmnpqrstvwxyz':
            list.append(frase_upp,str.upper(frase[i]))
        else:
            list.append(frase_upp, frase[i])
        i=i+1
    return str.join('', frase_upp)