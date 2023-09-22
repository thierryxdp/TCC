def retira_pontuacao(frase):
    interrogacao = frase.replace("?",' ')
    exclamacao = interrogacao.replace("!",' ')
    virgula = exclamacao.replace(",",' ')
    traco = virgula.replace("-",' ')
    dois_pontos = traco.replace(":",' ')
    ponto_virgula = dois_pontos.replace(";",' ')
    ponto_final = ponto_virgula.replace(".",' ')
    return ponto_final