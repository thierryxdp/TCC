def conta_frases(texto):
    "Funcao que conta o numero de frases que aparecem no texto."
    pontuacao = ['!','?','.']
    texto=texto.split()
    contador=0
    for laco_palavras in texto:
        for laco_pontuacao in pontuacao:
            if: laco_pontuacao in laco_palavras:
                contador+=1
                return contador