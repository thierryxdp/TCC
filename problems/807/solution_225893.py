def conta_frases(texto):
	"""Recebe um texto e retorna sua quantidade de frases; str->int."""
    pontos=str.count(texto,".")
    reticencias=str.count(texto,"...")
    exclamacoes=str.count(texto,"!")
    interrogacoes=str.count(texto,"?")
    if "..." in texto:
        return (pontos+reticencias+exclamacoes+interrogacoes)-3*reticencias
    else:
        return pontos+exclamacoes+interrogacoes