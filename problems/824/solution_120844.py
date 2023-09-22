def uppCons(frase):
    '''recebe uma frase e retorna a frase com todas as consoantes em maiusculas'''
    i = len(frase) - 1 #indice

    while i>=0:
        if frase[i] != 'a' and 'á' and 'à' and 'ã' and 'e' and 'é' and 'i' and 'í' and 'o' and 'ó' and 'õ' and 'u' and 'ú':
            maiusculo = str.upper(frase[i])
            frase = frase.replace(frase[i],maiusculo)

        i=i-1
    return frase