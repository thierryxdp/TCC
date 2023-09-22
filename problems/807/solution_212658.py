def contaFrase(texto):
    """
    Função que dado um texto conte e retorne a quantidade de frases nesse texto.
    Cada frase pode terminar com ponto final(.), ponto de interrogação(?), ponto de exclamação(!) ou reticências(...)
    Pontos de exclamação ou interrrogação não podem aparecer em sequência
    str-> int
    
    Parameters:
    texto: Paramêtro do tipo str que representa o texto inserido 
    
    """
    for pontoFinal in [ "!", "?", "...", "." ]:
        frases = str.count(frase, pontoFinal)
    return frases