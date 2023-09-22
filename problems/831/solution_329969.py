def lingua_p(palavra):
    palavraFinal = ''
    for letra in palavra:
        if letra in 'aáeéiíoúuAEIOU':
            palavraFinal = palavraFinal + letra + 'p' + letra
        else:
            palavraFinal = palavraFinal + letra
    return palavraFinal