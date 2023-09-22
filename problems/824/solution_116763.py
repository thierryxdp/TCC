def uppCons(frase):
    ''' funçao que recebe como entrada uma frase e retorna a
frase com todas as suas consoantes em maiusculas.
str -> str'''
    contador=0
    farse_upp='' 
    indice=len(frase)
    while contador < indice:
        if frase[contador]  in 'bcdfghjklmnpqrstvxwyz':
            farse_upp+=str.upper(frase[contador])
        else:
            farse_upp+= frase[contador]
        contador+=1
    return farse_upp