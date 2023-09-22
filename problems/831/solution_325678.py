def lingua_p (palavra):
    """Função que, dada uma palavra, retorna a mesma palavra, mas com a letra p após cada
    vogal da palavra original
    Entrada: string.
    Saída: string. """
    
    minuscula = str.lower(palavra)
    vogais = 'aeiou'
    idioma_p = ''
    
    for letra in minuscula:
        if letra in vogais:
            idioma_p = idioma_p + letra + 'p' + letra
        else:
            idioma_p = idioma_p + letra
    return idioma_p