def uppCons(frase):
    '''recebe uma frase e retorna a frase com as consoantes maiúsculas;string->string'''
    i=0
    vogais=['a','e','i','o','u','A','E','I','O','U']
    while len(frase)>i:
        if frase[i] not in vogais:
            maiuscula=str.upper(frase[i])
            reformed=frase.replace(frase[i],maiuscula)
            i+=1
        else:
            i+=1
    return reformed