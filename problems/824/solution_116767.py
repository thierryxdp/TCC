def uppCons(frase):
    ''' funçao que recebe como entrada uma frase e retorna a
frase com todas as suas consoantes em maiusculas.
str -> str'''
    contador=0
    frase_upp='' 
    indice=len(frase)
    while contador < indice:
        if frase[contador]  in 'bcdfghjklmnpqrstvxwyzç':
            frase_upp+=str.upper(frase[contador])
        else:
            frase_upp+= frase[contador]
        contador+=1
    return frase_upp