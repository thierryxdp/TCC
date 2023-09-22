def conta_frases(string:str)->int:
    
    """Função que conta o número de frases em uma string"""

    ponto = str.join("/", str.split(string,"."))
    exclamacao = str.join("/", str.split(ponto,"!"))
    interrogacao = str.join("/", str.split(esclamacao,"?"))
    reticencias = str.join("/", str.split(interrogacao,"..."))

    final = str.split(reticencias,"/ ")

    return len(final)