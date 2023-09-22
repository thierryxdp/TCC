#Exercício_02
''' Essa função recebe um string e retorna a mesma só que com as consoantes em maiúsculo. '''
''' str ---> str. '''

def uppCons(a):
    i = 0
    while i < len(a):
        z = a[i]
        w = str.upper(z)
        if a[i] in "cdfghjklmnpqrstvxywz":
            a = str.replace(a, z, w)
        i += 1
    return a