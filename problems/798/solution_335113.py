def freq_palavras(frases):
    '''recebe uma frase e conta quantas vezes derteminada palavras aparece naquela frase
    str->list'''
    palavras= []
    vezes_que_apareceu = {}
    for i in frases:
        if i not in range(palavras):
            palavras = palavras + [i]
            vezes_que_apareceu = vezes_que_apareceu + {palavras[i]: frases.count(i)}
    return vezes_que_apareceu