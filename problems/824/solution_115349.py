def uppCons(frase):
    '''retorna a frase recebida pela função
    com todas as suas consoantes maiúsculas;
    str -> str'''
    i=0
    letras=list(frase)
    while i<len(letras):
        if letras[i] not in 'aeiouãáéíóú ':
            letras[i]=letras[i].upper()
        i=i+1
    return ''.join(letras)