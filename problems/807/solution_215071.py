def quant_frases(texto):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    quant_frases = texto.count(".") + texto.count("!") + texto.count("?") + texto.count("...")
    return quant_frases