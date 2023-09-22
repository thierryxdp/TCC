def lingua_p(palavra):
    palavraFinal = ''
    for letra in palavra:
        if letra in 'aeéiíouAEIOU':
            palavraFinal = palavraFinal + letra + 'p' + letra
        else:
            palavraFinal = palavraFinal + letra
    return palavraFinal