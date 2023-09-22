def conta_frases(texto):
    """Dado um texto retorna a quantidade de frases nele.
    str -> int """

    exclamacao = texto.count("!")
    interrogacao = texto.count("?")
    pnt_final = texto.count(".")
    reticencias = texto.count("...") - texto.count(".") + 1
    
    pontos = exclamacao + interrogacao + pnt_final + reticencias
    
    
    return pontos