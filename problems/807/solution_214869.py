def quantidadeFrases(texto):
    """Funcao que recebe uma string contendo um texto e que conta a quantidade (numero
    inteirode frases que esse texto possui. Cada final de frase é determinado por um
    ponto final, ponto de exclamacao, interrogacao ou reticencias."""
    
    substituir = texto.replace("!",".")
    substituir = substituir.replace("?",".")
    substituir = substituir.replace("...",".")
    quantidade = substituir.count(".")
    return quantidade