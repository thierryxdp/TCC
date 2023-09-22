def uppCons(frase):
    '''Recebe uma frase e a retorna com todas as consoantes em maiúsculas
    sem modificar o restante dos caracteres
    string -> string'''
    indice = 0
    
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwyzBCDFGHJKLMNPQRSTVWYZ':
              return str.replace(frase, frase[indice], str.upper(frase[indice]))
        indice+= 1
    return frase1