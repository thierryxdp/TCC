def uppCons(frase):
    '''Retorna a frase com as suas consoantes maiúsculas
    	str -> str'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'aâãáàeêéèiûííoôõóòuûúùAÂÃÁÀEÊÉÈIÎÍÌOÒÓÕUÙÚÛ':
            frase = frase[:i] + str.upper(frase[i]) + frase[i+1:]
        i = i + 1
    return frase