def uppCons(frase):
    '''Função que recebe uma frase, e retorna a mesma com suas consoantes em maiúsculas;
    str -> str'''
    
    i=0
    consoante=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZçÇ':
            consoante=consoante+frase[i].upper()
        i+=1
    return frase