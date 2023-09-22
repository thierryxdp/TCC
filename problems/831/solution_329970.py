def lingua_p(palavra):
    """Retorna a palavra em linguagem de p;
    	str -> str"""
    palavraFinal = ''
    for letra in palavra:
        if letra in 'aáeéiíoúuAEIOU':
            palavraFinal = palavraFinal + letra + 'p' + letra
        else:
            palavraFinal = palavraFinal + letra
    return palavraFinal