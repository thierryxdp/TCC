def uppCons(frase):
    '''funcao que retorna a frase com suas consoantes maisculas;
    str->str'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            texto=texto+str.upper(frase[i])
        else:
             texto=texto+frase[i]
            i=i+1
    return texto