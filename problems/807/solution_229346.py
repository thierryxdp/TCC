def conta_frases(string):
    ''' funcao que, dado um texto em formato de string como parametro de entrada, retorne a quantidade de frases presentes neste texto
        str --> int '''
    
    acha_reticencias = str.find(string,'...')
    quantidade_ponto_final = str.count(string,'.')
    quantidade_ponto_interregocao = str.count(string,'?')
    quantidade_ponto_exclamacao = str.count(string,'!')
    
    
    if acha_reticencias == -1:
        
        return quantidade_ponto_final + quantidade_ponto_interregocao + quantidade_ponto_exclamacao
    
    else:
        return quantidade_ponto_final + quantidade_ponto_interregocao + quantidade_ponto_exclamacao + quantidade_ponto_tres_pontos