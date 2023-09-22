def lingua_p(palavra):
    palavraFinal = ''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            palavraFinal = palavraFinal + letra + 'p'
        else:
            palavraFinal = palavraFinal + letra
    return palavraFinal