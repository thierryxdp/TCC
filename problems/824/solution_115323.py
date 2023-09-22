def uppCons(texto):
    '''crie uma função que receba como entrada uma frase e retorne essa frase com todas as suas consoantes em maiusculas, sem alterar os demais caracteres. str-->str.'''
    indice=0
    frase_nova=''
    while indice<len(texto):
        if texto[indice] in 'bcçdfghjklmnpqrstvxz':
            frase_nova += str.upper(texto[indice])
        if texto[indice] not in 'bcçdfghjklmnpqrstvxz':
            frase_nova+=texto[indice]
        indice=indice+1
    return frase_nova