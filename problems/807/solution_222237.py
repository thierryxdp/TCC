def conta_frases(frases):
    if str.count(frases,'...') == True:
        return - 2*(str.count(frases,'...'))