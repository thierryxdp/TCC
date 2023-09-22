def lingua_p(palavra):
    palavraFinal = ''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            palavraFinal = palavraFinal + 'p' + letra
        else:
            palavraFinal = palavraFinal + letra
    return palavraFinal