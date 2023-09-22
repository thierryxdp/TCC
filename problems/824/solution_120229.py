def uppCons(frase):
    '''função que retorna todas consoantes maiúsculas e vogais como na frase original;
    str->str'''
    contador=0
    frase_nova=""
    while contador<len(frase):
        if str.lower(frase[contador]) in "bcdfghjklmnpqrstvwxyzç":
            frase_nova+=str.upper(frase[contador])
            contador+=1
        else:
            frase_nova+=frase[contador]
            contador+=1
    return frase_nova