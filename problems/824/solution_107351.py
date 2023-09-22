def uppCons(frase):
    '''Dada uma frase, retorne a mesma frase com todas as suas consoantes em maiúsculas, o resto como estava;
    str -> str'''
    frase=list(frase)
    indice=0
    f=[]
    while indice<len(frase):
        if  frase[indice] not in 'aeiouAEIOU':
            frase[indice]=str.upper(frase[indice])
            list.append(f,frase[indice])
        indice=indice+1
    return f