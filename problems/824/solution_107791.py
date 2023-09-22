def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas as suas consoantes em letras maiusculas sem alterar as vogais.
    str -> str'''
    i=0
    frase2=[]
    while i<len(frase):
        if frase [i] not in 'AaÁáàÀÃãÂâEeÉéêÊIiÌìíÍOoôÔõÕÓóuUúÚ':
            frase2= str.upper(frase[i])
        elif frase [i] in 'AaÁáàÀÃãÂâEeÉéêÊIiÌìíÍOoôÔõÕÓóuUúÚ':
            frase2= frase [i]
        i = i+1
    return frase2