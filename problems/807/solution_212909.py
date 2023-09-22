def conta_frases (texto):
    """Conta o numero de frases que vai em um texto.
    str -> int"""
    
    divisores = ['!', '?', '.']
    texto = texto.split ()
    contador = 0
    
    for palavras in texto:
        for pontos in divisores:
            if pontos in palavras:
                contador += 1
    
    return contador