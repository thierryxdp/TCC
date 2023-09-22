def uppCons (frase):
    FRASE = str.upper(frase)
    resposta = ''
    for caractere in FRASE:
        if caractere in 'AEIOUÃÕÉÀÁÉÍÓÚ':
            resposta += caractere.lower() 
        else: 
            resposta += caractere
    return resposta