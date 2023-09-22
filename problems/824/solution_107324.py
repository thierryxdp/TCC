def uppCons(frase):
    '''Dada uma frase, retorne a mesma frase com todas as suas consoantes em maiúsculas, o resto como estava;
    str -> str'''
    frase=list(frase)
    indice=0
    f=[]
    while indice<len(frase):
        if 'a','e','i','o','u','A','E','I','O','U' not in frase[indice]:
            list.append(f,frase[indice])
        indice=indice+1
    f=str(f)
    return f