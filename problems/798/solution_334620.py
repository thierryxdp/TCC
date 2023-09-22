def freq_palavras(frases):
    '''recebe uma frase e retorna um dicionário
    onde cada palavra da frase é uma chave e o valor
    da chave é o número d vezes que a palavra aparece.
    str -> dicionario'''
    frases = frases.split(' ')
    palavras = {}
    for num in frases:
        palavras[num] = frases.count(num)
    return palavras