def conta_frases(s):
    """conta a quantidade de frases em um texto de entrada"""
    x = ('!','?','.','...')
    for x in s:
        frases = len(str.split(s,x))