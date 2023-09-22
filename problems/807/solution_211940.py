def conta_frases(texto):
    '''Função que conta o número de frases que aparecem no texto introduzido como variável
string -> int'''

    Reticencias = "..."
    
    Reticencias2 = str.count(texto,Reticencias)
    Exclamacao = str.count(texto,"!")
    Interrogacao = str.count(texto,"?")
    Ponto = str.count(texto,".")
    
   	if Reticencias in texto:
        return (Reticencias2 + Exclamacao + Interrogacao + Ponto) - 3
    else:
        return Reticencias2 + Exclamacao + Interrogacao + Ponto