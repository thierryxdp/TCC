def conta_frases(frase):
    """Essa funcao recebe uma frase (str) e retorna a quantidade
de frases que ela possui (int) de acordo com as pontuacoes que
aparecem no final de cada uma (ponto final, exclamacao, interrogacao,
reticencias.
Obs: a linha frase.replace("..."," ") eh necessaria pois o str.count
confunde '...' como 3 '.', aumentando o numero de frases.
str -> int """
    quant_frases = 0
    quant_frases += frase.count("...") + frase.count("!") + frase.count("?")
    frase = frase.replace("..."," ")
    quant_frases += frase.count(".")
    return quant_frases