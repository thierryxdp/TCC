def conta_frases(texto):
    """Retorna o número de frases em um texto; str -> int"""
    exclamacao = str.split(texto,'!')
    juntar = str.join('.',exclamacao)
    reticencias = str.split(juntar,'...')
    juntar2 = str.join('.',reticencias)
    interrogacao = str.split(juntar2,'?')
    juntar3 = str.join('.',interrogacao)
    ponto = str.split(juntar3,'.')
    return len(ponto)-1