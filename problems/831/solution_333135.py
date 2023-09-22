def lingua_p (palavra):
    """recebe uma palavra em portugês e retorna essa palavra na língua do p. str ->str"""
    p1 = str.lower(palavra)
    palavrap= ""
    vogais ="aeiouàáéióôúâêãõ"
    for x in p1:
        palavrap += x
        if x in vogais:
            palavrap += "p" + x
    return palavrap