def lingua_p(text):
    """Recebe um texto e retorna traduzida na lingua p;
    str --> str"""
    
    vogais = "aeiou"
    buffer_text = ''

    for letra in text:
        if letra in vogais:
            buffer_text += str(letra + "p" + letra)
        else:
            buffer_text += str(letra)

    return buffer_text