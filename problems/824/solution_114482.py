def uppCons(frase):
    '''a funcao recebe uma frase e retorna a frase orifinal com as consoantes em maiusculo;
    str->str'''
    frase1=''
    x=0
    while x<len(frase):
        if not frase[x] in 'aeiou':
            frase1=frase1+max(frase[x])
        else:
            frase1=frase1+frase[x]
        x=x+1
    return frase1