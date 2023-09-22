def conta_frases(texto):
    """Conta a quantidade de palavras em um texto;
    string -> int"""
    in texto str.remove(",","!",".","...","?")
    return len(str.split(texto))