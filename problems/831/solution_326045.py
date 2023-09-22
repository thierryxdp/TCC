def lingua_p(frase):
    """Função que recebe uma palavra como parametro e retorna a 
    mesma traduzida para a lingua do P. Que é quando apos uma
    vogal da é inserida a letra 'p'
    str -> str"""
    vogais = 'ãaáàeéèiíoóuú'
    vogais_lower = str.lower(vogais)
    palavra = ''

    for letra in frase:
        if letra in vogais:
            palavra = palavra +  letra + 'p' + letra
            
        elif letra in vogais_lower:
            palavra = palavra +  letra + 'p' + letra
            
        else:
            palavra = palavra + letra

    return palavra