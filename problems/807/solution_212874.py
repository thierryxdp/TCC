def conta_frases(texto):
    """Função para determinar a quantidade de frases em um determinado texto.
       Onde: "texto" - é o texto em que se deseja determinar o número de frases.
    srt -> str"""
    exclamacao = texto.count('!')
    interrogacao = texto.count('?')
    reticencias = texto.count('...')
    ponto = texto.count('.')
    numero_frases = exclamacao + interrogacao + reticencias + ponto
    if reticencias > 0:
        numero_frases -= 3 * reticencias
    return numero_frases