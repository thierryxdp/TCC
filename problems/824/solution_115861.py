def uppCons(frase):
    '''Função que recebe uma frase, e retorna a mesma com suas consoantes em maiúsculas;
    str -> str'''
    
    i=0
    consoante=''
    while i<len(frase) and caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            consoante+=caractere.upper()
        else:
            consoante+= caractere
        i+=1
    return consoante
print (uppCons('abcdef'))