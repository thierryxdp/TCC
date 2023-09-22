def conta_frases(texto):
    """Dada um texto, a função conta e retorna a quantidade
    de frases desse texto.
    Parametro de entrada: str
    Retorna: int"""

    auxiliar= texto.replace('?','.')
    auxiliar= auxiliar.replace('!','.')
    auxiliar= auxiliar.replace('...','.')

    auxiliar2= auxiliar.split('.')
    tamanho= len(auxiliar2)

    return tamanho-1