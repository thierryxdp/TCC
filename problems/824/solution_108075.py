def uppCons(frase):
    '''Dada uma frase, retorne a mesma frase com todas as suas consoantes em maiúsculas, o resto como estava;
    str -> str'''
    indice=0
    n=''
    while indice<len(frase):
        if frase[indice] not in 'aeiouAEIOUãáâéêi':
            a=str.upper(frase[indice])
            n=n+a
        else:
            n=n+frase[indice]
        indice=indice+1
    return n