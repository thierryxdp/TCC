def conta_frases(Texto=''):
    
    Pontos_Finais = conta_frases.count('.')
    Ponto_Exclamacao = conta_frases.count('!')
    Ponto_Interrogacao = conta_frases.count('?')
    Pontos_Reticencias = conta_frases.count('...')
    
    Numero_frases = (Pontos_Finais + Ponto_Exclamacao + 
                     Ponto_Interrogacao + Pontos_Reticencias)
    
    return Numero_frases