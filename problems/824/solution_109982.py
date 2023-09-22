def uppCons(frase):
    '''Função que dada uma frase (frase) retorna a mesma frase
    com todas as consoantes em maiúsculo.
    str->str'''
    novafrase=''
    i=0
    consoantes= 'bcdfghjklmnpqrstvwxyzç'
    
    while i < len(frase):
        if frase[i] in consoantes:
            novafrase=novafrase+ str.upper(frase[i])
            
        else:
            novafrase= novafrase+frase[i]
        
        i=i+1
        
    return novafrase