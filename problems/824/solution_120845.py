def uppCons(frase):
    '''recebe uma frase e retorna a frase com todas as consoantes em maiusculas'''
    i = len(frase) - 1 #indice

    while i>=0:
        if frase[i] != 'a' and frase[i] != 'á' and frase[i] != 'à' and frase[i] != 'ã' and frase[i] != 'e' and frase[i] != 'é' and frase[i] != 'i' and frase[i] !='í' and frase[i] !='o' and frase[i] !='ó' and frase[i] !='õ' and frase[i] !='u' and frase[i] !='ú':
            maiusculo = str.upper(frase[i])
            frase = frase.replace(frase[i],maiusculo)

        i=i-1
    return frase