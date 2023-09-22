def conta_frases(texto):
    pontuacao = "!","?",".","..."
    for car in pontuacao:
        texto = texto.replace(car, "#")
     
    x = texto.split ("#")
    return len(x)