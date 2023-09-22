def conta_frases(frase):
    type(frase) == str
    ocorrencias_de_exclamacao=str.count(frase,"!")
    ocorrencias_de_interrogacao=str.count(frase,"?")
    ocorrencias_de_pontos=str.count(frase,".")
    if "..." in frase:
        ocorrencias_de_pontos=str.count(frase,".")//2
    numero_total = ocorrencias_de_pontos+ocorrencias_de_exclamacao+ocorrencias_de_interrogacao
    return numero_total