def conta_frases(texto):
    """dada um texto, essa função contará a quantidade de frases presentes nele
    string--->int"""
    return str.count(texto,"!")+str.count(texto,"?")+str.count(texto,"...")+str.count(texto,".")-3*str.count(texto,"...")