def uppCons(frase):
    '''Retorna a frase com todas as suas consoantes em maiúscula;
    str -> str'''
    i=0
    frase_upp=''
    while i<len(frase):
        if frase[i] in 'AEIOUaeiouÁÉÍÓÚáéíóúãõêâ':
            frase_upp=frase_upp+frase[i]
        else:
            frase_upp=frase_upp+str.upper(frase[i])
        i=i+1
    return frase_upp