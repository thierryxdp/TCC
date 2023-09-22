def uppCons(frase):
    '''recebe uma frase e retorna a frase com todas as consoantes em maiusculas'''
    i = len(frase) - 1 #indice

    while i>=0:
        if frase[i] != 'a' or 'á' or 'à' or 'ã' or 'e' or 'é' or 'i' or 'í' or 'o' or 'ó' or 'õ' or 'u' or 'ú':
            maiusculo = str.upper(frase[i])
            frase = frase.replace(frase[i],maiusculo)
            if i == 0:
                frase=frase.replace(frase[i],maiusculo)
        i=i-1
    return frase