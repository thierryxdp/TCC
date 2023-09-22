def uppCons (frase):
    '''
       Função que recebe uma frase (frase) e retorna essa
       frase com todas as consoantes maiúsculas.
       str -> str
    '''
    upp=''
    i=0
    while i<len(frase):
        cons = 'bcdfghjhlmnpqrstvwxyz'
        if frase[i] in cons:
            frase = frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase