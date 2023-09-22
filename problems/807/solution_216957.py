def conta_frases(frases):
    '''Função que dado um texto de entrada conte quantas frases
    o mesmo contém, levando em consideração que cada frase é 
    finalizada com '.','!','?','...'
    string --> int'''
    frases = frases.replace("!",".")
    frases = frases.replace("...","?")
    return len(frases)