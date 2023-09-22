def uppCons(frase):
#Funcao que recebe como entrada uma frase e retorna as consoantes em maiuscula
    i=0
    nova_frase=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            nova_frase+=frase[i].upper()
        else:
            nova_frase+=frase[i]
        i+=1
    return nova_frase