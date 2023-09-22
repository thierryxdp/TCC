def conta_frases(texto):
    reticencias= str.count(texto,"...")
    pontos= str.count(texto,".")
    ponto_final= pontos - reticencias*3
    interrogacao= str.count(texto,"?")
    exclamacao= str.count(texto,"!")
    resultado= reticencias + ponto_final + interrogacao + exclamacao
    return resultado