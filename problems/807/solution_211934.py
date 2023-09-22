def conta_frases(texto):
    '''Função que conta o número de frases que aparecem no texto introduzido como variável
string -> string'''

    Reticencias = str.count(texto,"...")
    Exclamacao = str.count(texto,"!")
    Interrogacao = str.count(texto,"?")
    Ponto = str.count(texto,".")

    return TresPontos + Exclamacao + Interrogacao + Ponto