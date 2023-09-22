def conta_frases(texto):
    """função que conta o número de frases que aparecem no texto;
    Entrada: str
    Saída: int"""
     texto=str.replace(texto,'?','.')
     texto=str.replace(texto,'!','.')
     texto=str.replace(texto,'...','.')
     f=str.count(texto,'.')
     return f