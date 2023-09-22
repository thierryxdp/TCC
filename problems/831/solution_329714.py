def lingua_p(palavra):
    frase=0
    vogais='aeiouAEIOU'
    for i in palavra:
        if i in vogais:
            posicao=str.find(palavra,vogais)
            'p'.join(palavra,posicao)
        frase=frase+1

    return frase