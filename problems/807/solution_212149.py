def conta_frases(texto):
    """
    Calcula a quantidade de frases em um texto, levando em consideração que cada frase
    é terminada em uma das seguintes pontuações: ponto final, ponto de exclamação, ponto
    de interrrogação ou reticências.
    str -> int.

    Parameters:
    frase: Parâmetro textual, do tipo string (str);
    
    Returns:
    A quantidade de frases em um texto.
    """
    
    pontuacoes = (".","!","?","...")

    reticencias = (str.count(texto,pontuacoes[3]))
    pontos = (str.count(texto,pontuacoes[0]) - reticencias * 3)
              
    
    total_frase =  (pontos + str.count(texto,pontuacoes[1]) + str.count(texto,pontuacoes[2]) + reticencias)
    return total_frase