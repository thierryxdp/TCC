def lingua_p (palavra):
    """Função que dada uma palavra e retorna a palavra traduzida para a lingua do P.
    str -> str"""
     vogais = 'ãaáàeéèiíoóuú'
    vogaisup = str.upper(vogais)
    palavra_p = ''
    for letra in palavra:
        if letra in vogais:
            palavra_p = palavra_p +  letra + 'p' + letra     
        elif letra in vogaisup:
            palavra_p = palavra_p +  letra + 'p' + letra   
        else:
            palavra_p = palavra_p + letra
    return str.lower(palavra_p)