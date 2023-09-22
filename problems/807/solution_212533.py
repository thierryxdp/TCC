def conta_frases(texto):
    """A função conta o número de frases que aparecem no texto dado;
       str->int
       Parametro:
       texto: texto dado 
    """
    ponto = str.join("/", str.split(texto,"."))
    exclamacao = str.join("/", str.split(ponto,"!"))
    interrogacao = str.join("/", str.split(exclamacao,"?"))
    reticencias = str.join("/", str.split(interrogacao,"..."))

    final = str.split(reticencias,"/ ")

    return len(final)