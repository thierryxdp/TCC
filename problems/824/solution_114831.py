def uppCons(frase):
    '''funcao que recebe uma frase e retorna essa frase com
    todas as consoantes em letra maiuscula
    str->str'''
    string= ''
    proximo=0
    while proximo<len(frase):
        if frase[proximo] not in 'AEIOUaeiouãÃúÚoÓ':
            string= string + str.upper(frase[proximo])
        if frase[proximo] in 'aeiouAEIOUÃãúÚoÓ':
            string= string + frase[proximo]
        proximo= proximo +1
    return string