def uppCons(frase):
    '''dada uma frase, retorna a mesma com suas consoantes em letra maiuscula
str-->str'''
    frase_upcons=''
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiouÁÉÍÓÚáéíóúâêÂÊÀàãÃõÕ':
            frase_upcons+=str.upper(frase[i])
        else:
            frase_upcons+=frase[i]
        i+=1
    return frase_upcons