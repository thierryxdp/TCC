def uppCons(frase):
    '''função que recebe uma frase e retorna a mesma frase, mas com todas
    as consoantes em maiúsculas; str -> str'''
    i = 0
    cons = ''
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouÁÀÂÃÉÊÍÓÔÕÚáàâãéêíóôõú':
            cons = cons + frase[i]
        i = i + 1
    return cons