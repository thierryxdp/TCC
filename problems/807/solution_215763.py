def conta_frases(string):
    """Recebe uma string e retorna a quantidade 
    	de frases que esta possue baseado na 
        ocorrência de pontos separadores
        str -> int"""
    excla = string.count("!")
    ponto = string.count(".")
    inter = string.count("?")
    ret = string.count("...")
    ponto = ponto - ret*3
    return excla + ponto + inter + ret