def conta_frases (texto):
    """dado um texto string como entrada, retorna o número de frases que ele possuí;
    str->int"""
    teste = 0
    texto = texto.replace("...",".")
    teste = teste + str.count(texto, "!", 0,)
    teste = teste + str.count(texto, "?", 0, )
    teste = teste + str.count(texto, ".", 0, )

    return (teste)