def lingua_p(frase):
    """retorna a para a lingua do p, ou seja,inserir
    apos vogal a letra p a sequencia de p mais a vogal
    str -> str"""
    vogais = 'ãaáàeéèiíoóuú'
    vogaisup = str.upper(vogais)
    palavra = ''
    for letra in frase:
        if letra in vogais:
            palavra = palavra +  letra + 'p' + letra

        elif letra in vogaisup:
            palavra = palavra +  letra + 'p' + letra

        else:
            palavra = palavra + letra
    return str.lower(palavra)