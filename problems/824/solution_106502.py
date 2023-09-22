def uppCons(frase):
    '''recebe uma frase e retorna a frase com as consoantes maiúsculas;string->string'''
    i=1
    vogais=['a','e','i','o','u','A','E','I','O','U']
    lista_frase=str.split(frase)
    join_frase=str.join(' ',frase)
    lista_letra=list(join_frase)
    maiuscula_frase=str.upper(frase)
    lista_maiuscula=str.split(maiuscula_frase)
    join_maiuscula=str.join(' ', maiuscula_frase)
    lista_maiuscula=list(join_maiuscula)
    while len(frase)>i:
        if lista_letra[i] not in vogais:
            lista_letra[i]=lista_maiuscula[i]
            i+=1
        else:
            i+=1
    return str.join('',str.split(lista_letra))