def lingua_p(mensagem):
    mensagem = mensagem.lower()
    traducao = mensagem

    for letra in mensagem: #valer
        if (letra in 'aeiou'):
            particao = traducao.partition(letra)
            traducao = particao[0] + letra + 'p' + particao[1] + particao[2]

    return traducao