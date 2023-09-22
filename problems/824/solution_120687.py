def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma frase em letra maiuscula'''
    n = len(frase) - 1

    while n >=0:
        
        if frase[n] != 'a' and frase[n] != 'á' and frase[n] != 'à' and frase[n] != 'ã' and frase[n] != 'e' and frase[n] != 'é' and frase[n] != 'i' and frase[n] != 'í' and frase[n] != 'o' and frase[n] != 'ó' and frase[n] != 'õ' and frase[n] != 'u' and frase[n] != 'ú':
            caracter = str.upper(frase[n])
            frase=frase.replace(frase[n],caracter,n)
        n=n-1

    return frase