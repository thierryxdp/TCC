def inverte(frase):
    """
    Código que inverte a ordem de palavras da entrada frase
    sem letras maiúsculas e sem pontuação.
    :Frase --> String:
    :Return--> String:
    """
    frase_v1 = frase.lower()
    frase_v2 = frase_v1.strip('!')
    frase_v3 = frase_v2.strip('?')
    frase_v4 = frase_v3.strip('.')
    frase_v5 = frase_v4.strip(':')
    frase_v6 = frase_v5.strip(';')
    frase_v7 = frase_v6.strip(',')
    frase_v8 = frase_v7.strip('-')
    frase_v9 = frase_v8.replace(',','')
    frase_tech= frase_v9.split()
    frase_v10 = (frase_tech[::-1] for frase_v9 in frase_tech)
    frase_new =str(frase_tech[::-1]) 
    frase_tech.join('')   
    return