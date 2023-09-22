def uppCons(frase):
    '''funcao que recebe uma frase e retorna a mesma frase só que com todas as consoantes em maiusculas;
    str->str'''
    novafrase= ''
    i= 0
    while i<len(frase):
        if frase[i] in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZzÇç':
            novafrase= novafrase+str.upper(frase[i])
        else:
            novafrase= novafrase+frase[i]
        i= i+1
     
    return novafrase