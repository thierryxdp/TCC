def freq_palavras(frases):
    '''funcao que recebe uma str e retorna um dict em que cada palavra da str seja uma chave e tenha o valor de quantas vezes essa palavra se repetiu
    str->dict'''
    chaves=dict()
    frases=frases.split('')
    for palavras in frases:
        if palavras not in chaves:
            chaves[palavras]=1
        else:
            chaves[palavras]+=1
    return chaves