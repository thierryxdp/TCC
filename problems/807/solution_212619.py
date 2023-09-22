def conta_frases(texto):
    """retorna quantas frases tem em um texto, dado o texto. as frases são dividas por, ".","...","?" e "!".
    string->int"""
    return texto.count("?")+texto.count(".")+texto.count("...")+texto.count("!")-(texto.count("...")*3)