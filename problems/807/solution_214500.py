def conta_frases(texto):
    """Conta a quantidade de palavras em um texto;
    string -> int"""
    return len(str.split(texto)) - len(texto.count(".","!","...","?"))