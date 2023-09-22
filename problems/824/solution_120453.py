def uppCons (frase):
    FRASE = str.upper(frase)
    resposta = ''
    for caractere in FRASE:
        if caractere in 'AEIOU':
            resposta += caractere.lower() 
        else: 
            resposta += caractere
    return resposta