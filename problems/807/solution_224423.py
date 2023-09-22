def conta_frases(texto):
    """retorna a quantidade de frases presentes em um texto;
    str -> int"""
    pontuacao=str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')
    if '...'in texto:
        return pontuacao-2*str.count(texto,'...')
    else:
        return pontuacao