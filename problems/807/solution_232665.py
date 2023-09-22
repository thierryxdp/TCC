def conta_frases(texto):
   
    ponto = texto.count(".")
    interrogacao = texto.count("!")
    exclamacao = texto.count("?")
    reticencias = texto.count("...")
    frasecomreticencias = (reticencias*3)
    if "..." in texto:
        return (ponto+interrogacao+exclamacao+reticencias-frasecomreticencias)
    else:
        return (ponto+interrogacao+exclamacao)