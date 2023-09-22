def uppCons(frase):
 '''função que recebe uma frase e retorna essa frase com todas as suas consoantes em maisculas e os
    demais caracteres exatamente como estavam na frase original;
    sting-> string'''
while i < len(frase):
    if frase[i] in 'bcdfghjklmnpqrstvwxz':
        frase_nova = frase_nova+ str.upper(frase[i])
    else:
        frase_nova = frase_nova+ frase[i]
    i=i+1
return frase_nova