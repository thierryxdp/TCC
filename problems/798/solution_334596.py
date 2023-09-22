def freq_palavras(frases):
    '''recebe uma frase e retorna um dicionário
    onde cada palavra da frase é uma chave e o valor
    da chave é o número d vezes que a palavra aparece.
    str -> dicionario'''
    frases = frase.split(' ')
    palavras = {}
    for num in frase:
        if frase[num] not in palavras:
        	vezes = list.count(frase, num)
        	palavras[frase] = vezes
    return palavras