def uppCons(frase):
    '''funcao que recebe uma frase como entrada e retorna a mesma frase com todas as consoantes em maiusculas
    str -> str'''
    i=0
    frase_saida=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
            frase_saida=frase_saida+frase[i]
        else:
            frase_saida=frase_saida+frase[i]
        i=i+1
    return frase_saida