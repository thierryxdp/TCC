def conta_frases(texto):
    '''Função que conta o número de frases que aparecem no texto introduzido como variável
string -> int'''

    Reticencias = str.count(texto,"...")
    Exclamacao = str.count(texto,"!")
    Interrogacao = str.count(texto,"?")
    Ponto = str.count(texto,".")
    PontoFinal = Ponto - Reticencias*3
    
    return Reticencias + Exclamacao + Interrogacao + PontoFinal