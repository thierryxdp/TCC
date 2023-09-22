def conta_frases(txt):
    """da um texto e retorna a qntdd de frases nele, considerando "...", ".",
    "?" e "!" como intervalos entre frases
    linha de pensamento:
    olha... maneiro.
    resposta esperada = 2; resposta recebida 5
    3 e 1 + 1
    
    olha... maneiro?
    resposta esperada = 2; resposta recebida 5
    3 e 1 + 1
    3 - 1 + 1
    se fizer a qntdd de . menos o dobro da qntdd de reticencias deve dar certo
    
    str -> int
    """
    return txt.count("!") + txt.count("?") + (txt.count(".") - txt.count("...")*2)