def conta_frases (texto):
    """funçao que recebe um texto e retorna a quantidade de frases que aparecem no texto baseada na pontuaçao do mesmo;
entrada: str
saida: int."""

    texto = str.replace (texto, '...', '.')

    frases = str.count (texto, '.')
    frases = frases + str.count (texto, '!')
    frases = frases + str.count (texto, '?')

    return frases