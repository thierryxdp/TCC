def uppCons(frase):
    """Recebe uma frase e retorna-a com suas consoantes em maiúsculo

    str -> str"""
    frase2 = ''
    i = 0
    while (i < len(frase)):
        if frase[i] in 'aãáäâeéêëiíîïoóôõöuúûüAÁÃÂÄEÉÊËIÍÎÏOÓÕÔÖUÚÛÜ':
            frase2 += frase[i]
        else:
            frase2 += str.upper(frase[i])
        i += 1
    return frase2