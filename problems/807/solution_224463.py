def conta_frases(texto):
    """Dado um texto retorna a quantidade de frases nele.
    str -> int """

    exclamacao = texto.count("!")
    interrogacao = texto.count("?")
    reticencias1 = texto.count("a...")
    reticencias2 = texto.count("e...")
    reticencias3 = texto.count("i...")
    reticencias4 = texto.count("o...")
    reticencias5 = texto.count("u...")
    
    pnt_final = texto.count('. ')
     
     
    
    pontos = exclamacao + interrogacao + pnt_final  + reticencias1 + reticencias2 + reticencias3 + reticencias4 + reticencias5
    
    
    return pontos