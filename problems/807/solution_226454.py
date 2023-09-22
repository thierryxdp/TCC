def conta_frases(frase):
    type(frase) == str
    frase.replace("...",".")
    ocorrencias_de_exclamacao=str.count(frase,"!")
    ocorrencias_de_interrogacao=str.count(frase,"?")
    ocorrencias_de_pontos=str.count(frase,".")
    numero_total = ocorrencias_de_pontos+ocorrencias_de_exclamacao+ocorrencias_de_interrogacao
    return numero_total