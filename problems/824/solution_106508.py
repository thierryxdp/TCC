def uppCons(frase):
    '''recebe uma frase e retorna a frase com as consoantes maiúsculas;string->string'''
    i=0
    vogais=['a','e','i','o','u','A','E','I','O','U','ã','Ã','À','à','Á','á','é','É','í','Í','ó','Ó','ú','Ú']
    lista_frase=list(frase)
    maiuscula_frase=str.upper(frase)
    lista_maiuscula=list(maiuscula_frase)
    while len(frase)>i:
        if frase[i] not in vogais:
            lista_frase[i]=lista_maiuscula[i]
            i+=1
        else:
            i+=1
    return str.join('',lista_frase)