def retira_pontuacao(frase):
    virgula = frase.replace(",",' ')
    traco = virgula.replace("-",' ')
    dois_pontos = traco.replace(":",' ')
    ponto_virgula = dois_pontos.replace(";",' ')
    ponto_final = ponto_virgula.replace(".",' ')
    return ponto_virgula