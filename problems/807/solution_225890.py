def conta_frases(texto):
	"""Recebe um texto e retorna sua quantidade de frases; str->int."""
    pontos=str.count(texto,".")
    reticencias=str.count(texto,"...")
    exclamacoes=str.count(texto,"!")
    interrogacoes=str.count(texto,"?")
        return pontos+exclamacoes+interrogacoes+reticencias