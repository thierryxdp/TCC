def conta_frases(texto):
    """ Função que recebe um texto, em forma de string, e retorna o numero de frases nele contido """
    interrogacao = str.count(texto, "?")
    exclamacao = str.count(texto, "!")
    redicencias = str.count(texto, "...")
    pontoFinal  = str.count(texto, ".") - redicencias*3
    pontos = interrogacao + exclamacao + redicencias + pontoFinal
    return pontos