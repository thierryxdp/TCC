def conta_frases(texto):
    """Conta a quantidade de frases em um texto.
       str->int
       
       Parameters:
       texto: O texto do qual as frases serão contadas.
       
       Returns:
       O número de frases no texto.
       """
    return texto.count('!')-2*texto.count('...')+texto.count('.')+texto.count('?')