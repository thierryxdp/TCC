def conta_frases(texto):
    """Com um texto como entrada, retorna a quantidade de frases separadas por ponto final,
    exclamação, interrogação ou reticências.
    assinatura: str --> int
    testes:
    conta_frases("O dia clareou! Que bom!")==2
    conta_frases("A noite será longa. Trouxe um baralho? Que pena...)==3
    """
    exclam = str.count(texto, "!")
    pfim = str.count(texto, ".") - 3* retic
    interrog = str.count(texto, "?")
    retic = str.count(texto, "...")
    return exclam + interrog + retic + pfim