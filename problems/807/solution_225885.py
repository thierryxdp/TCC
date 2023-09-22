def conta_frases(texto):
	"""Recebe um texto e retorna sua quantidade de frases; str->int."""
	pontos=str.count(texto,".")
    exclamacoes=str.count(texto,"!")
    reticencias=str.count(texto,"...")
    interrogacoes=str.count(texto,"?")
    n_frases=pontos+exclamacoes+reticencias+interrogacoes
    return n_frases