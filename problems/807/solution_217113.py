def conta_frases(texto):
    """Função que retorna o numero de frases dado um certo texto
    string --> int """
    texto= str.replace(texto)
    return len(str.split(texto))-1