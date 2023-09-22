def quant_frases(texto):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    return (texto.count(".") + texto.count("!") + texto.count("?") + texto.count("..."))