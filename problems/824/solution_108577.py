def uppCons(frase):
    '''funcao que recebe uma frase e retorna a mesma com
    todas as consoantes em letra maiuscula.
    str --> str'''
    nova_frase = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            #print(frase[i])
            n = frase[i].upper() #variavel q muda sempre que roda
            nova_frase += n
            i += 1
        
        else:
            #print(frase[i])
            nova_frase += frase[i]
            i += 1
    return nova_frase