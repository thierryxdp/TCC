def uppCons(frase):
    '''Função que recebe uma frase, e retorna a mesma com suas consoantes em maiúsculas;
    str -> str'''
    
    i=0
    letras=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZçÇ':
            letras=letras+frase[i].upper()
        else:
            letras=letras+frase[i]
        i+=1
    return letras