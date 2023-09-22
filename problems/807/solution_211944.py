def conta_frases(texto):
    '''Função que conta o número de frases que aparecem no texto introduzido como variável
string -> int'''

    Exclamacao = str.count(texto,"!")
    Interrogacao = str.count(texto,"?")
    Ponto = str.count(texto,".")
    Reticencias = Ponto*3
    
    return Reticencias + Exclamacao + Interrogacao + (Ponto - Reticências)