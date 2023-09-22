def conta_frases(string):
    ''' funcao que, dado um texto em formato de string como parametro de entrada, retorne a quantidade de frases presentes neste texto
        str --> int '''
    
    quantidade_ponto_final = str.count(string,'.')
    quantidade_ponto_interregocao = str.count(string,'?')
    quantidade_ponto_exclamacao = str.count(string,'!')
    quantidade_ponto_tres_pontos = str.count(string,'...')
    
    quantidade_frases = quantidade_ponto_tres_pontos + quantidade_ponto_exclamacao + quantidade_ponto_interregocao + quantidade_ponto_final 
    
    return quantidade_frases