def conta_frases (texto):
    """dado um texto string como entrada, retorna o número de frases que ele possuí;
    str->int"""
    
    teste1 = str.count(texto, "!", 0,)
    teste2 = str.count(texto, "?", 0, )
    teste3 = str.count(texto, ".", 0, )
    teste4= str.count(texto, "...", 0, )
    teste = teste1 + teste2 + teste3 + teste4
           

    return (teste)