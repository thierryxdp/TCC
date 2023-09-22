def uppCons(frase):
    ''' recebe uma frase e deixa todas as suas consoante maiusculas
    str->str'''
    list(frase)
    i=0
    while i<len(frase):
        if frase[i] not "AEIOUaeiou":
            frase[i].uppper()
        i=i+1
    return ' '.join(frase)