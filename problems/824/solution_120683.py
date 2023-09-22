def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase em letra maiuscula'''
    n = len(frase)

    while n >=0:
        n=n-1
        if frase[n] != ('a' and 'ã') and frase[n] != 'e' and frase[n] != 'i' and frase[n] != 'o' and frase[n] != 'u':
            caracter = str.upper(frase[n])
            frase=frase.replace(frase[n],caracter,n)

    return frase