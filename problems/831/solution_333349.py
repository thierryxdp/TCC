def lingua_p(mensagem):
    mensagem = mensagem.lower()
    traducao = ''
    aux = 0
    
    for letra in mensagem:
        if letra in 'aeiouãáéíóúâêîôû':
            i = mensagem.index(letra,aux)
            traducao += mensagem[aux:i+1] + 'p' + letra
            aux = i+1
    
    resto = mensagem - traducao
    traducao += resto
    
    return traducao