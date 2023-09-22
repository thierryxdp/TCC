def uppCons(frase):
    '''recebe uma frase e retorna a frase com as consoantes maiúsculas;string->string'''
    i=1
    vogais=['a','e','i','o','u','A','E','I','O','U']
    lista_frase=list(frase)
    maiuscula_frase=str.upper(frase)
    lista_maiuscula=list(maiuscula_frase)
    while len(frase)>i:
        if frase[i] not in vogais:
            lista_frase[i]=lista_maiuscula[i]
            i+=1
        else:
            i+=1
    return lista_frase