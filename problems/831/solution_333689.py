def lingua_p(mensagem):
    mensagem = mensagem.lower()
    traducao = mensagem

    for i in range(0, len(mensagem)):
        letra = mensagem[i]
        if (letra in 'aeiou'):
            j = traducao.find(letra, i) + 1
            traducao = traducao[:j] + letra + 'p' + traducao[j:]
        
    return traducao