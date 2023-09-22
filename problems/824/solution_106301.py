def uppCons(frase):
    '''funcao que recebe uma frase e retorna essa mesma frase com todas as suas consoantes em maiuscula
    str->str'''
    i = 0
    consoantes=()
    while i<len(frase):
        if frase[i] in 'qrtpsdfghjklzxcvbnm':
            frase=str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase