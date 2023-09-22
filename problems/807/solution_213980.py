def conta_frases(texto):
    """Funcao que conta o numero de frases que aparecem no texto;
    Entrada: str
    Saida: int"""

    Inter = str.count(texto,'?')
    Excla = str.count(texto,'!')
    Retic = str.count(texto,'...')
    Ponto = str.count(texto,'.')-Retic*3
    frases = Inter + Excla + Retic + Ponto

    return frases