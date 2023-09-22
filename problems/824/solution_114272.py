def uppCons(frase):
    '''função que recebe uma frase(string) como entrada e retorna uma
    nova frase em string, mudando todas as consoantes da frase de entrada
    para a forma maiúscula e mantendo os outros caracteres originais;
    string->string'''
    
    i=0
    final=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            final=final + str.upper(frase[i])
        else:
            final=final+ frase[i]
        i=i+1
    return final