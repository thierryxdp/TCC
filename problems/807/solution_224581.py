def conta_frases(frases):
    """Dado um texto armazenado em uma string, a função retorna o número de frases que aparecem no texto."""
    """str->int"""
    if frases[-3:len(frases)] == "...":
        return str.count(frases,". ") + str.count(frases,"!") + str.count(frases,"?") + str.count(frases,"...")
    else:
        return str.count(frases,".",-1,len(frases)) + str.count(frases,". ") + str.count(frases,"!") + str.count(frases,"?") + str.count(frases,"...")