def conta_frases(Texto=''):
    
    Pontos_Finais = Texto.count('.')
    Ponto_Exclamacao = Texto.count('!')
    Ponto_Interrogacao = Texto.count('?')
    Pontos_Reticencias = Texto.count('...')
    
    Numero_frases = (Pontos_Finais + Ponto_Exclamacao + 
                     Ponto_Interrogacao + Pontos_Reticencias)
    
    return Numero_frases