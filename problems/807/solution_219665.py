def conta_frases (texto):def conta_frases (texto):
    """dado um texto string como entrada, retorna o número de frases que ele possuí;
    str->int"""
    for n in texto:
        teste= []

        if texto.split("!"):
            teste= teste+ ['a']
        if texto.split("?"):
            teste=teste + ['a']
        if texto.split("..."):
            teste=teste + ['a']
        if texto.split("."):
            teste=teste + ['a']
    
    return len(teste)