def lingua_p(mensagem):
    mensagem = mensagem.lower()
    traducao = []
    mensagem_traduzida = ''

    for i in range(0, len(mensagem)):
        letra = mensagem[i]
        traducao.append(letra)
        if (letra in 'aeiouáéíóúâêîôûãõ'):
            traducao.append('p')
            traducao.append(letra)

    for i in range(0,len(traducao)):
        mensagem_traduzida = mensagem_traduzida + traducao[i]
        
    return mensagem_traduzida