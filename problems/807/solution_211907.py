#Q2 - Conta Frases

def conta_frases(texto):
    '''Função que conta o número de frases que aparecem no texto introduzido como variável
string -> string'''

    Reticencias = "..."
    TresPontos = str.count(texto,Reticencias)
    Exclamacao = str.count(texto,"!")
    Interrogacao = str.count(texto,"?")
    Ponto = str.count(texto,".")

    return Reticencias + Exclamacao + Interrogacao + Ponto