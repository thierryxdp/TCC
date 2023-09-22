def lingua_p(palavra):
    """Funcao que traduz uma palavra em portugues para a Lingua do P 
    e retorna a palavra traduzida; str -> str"""
    
    acumulador = ""
    palavra = str.lower(palavra)
    
    for letra in palavra:
        if letra in "aeiouáàãâéèêíìîóôòõúùû":
            acumulador = acumulador + letra + "p" + letra
        else:
            acumulador = acumulador + letra
    return acumulador