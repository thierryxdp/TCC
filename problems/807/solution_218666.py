def conta_frases(texto):
    for pontuacao in "...,!,?,.":
        texto = texto.replace(pontuacao,"1")