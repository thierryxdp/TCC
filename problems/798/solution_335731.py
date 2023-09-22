def freq_palavras(frases):
    '''retorna um dicionario com as palavras e a qnt de vezes que se repetem'''
    from collections import Counter
    cnt = Counter()
    for Word in [frases]:
        cnt[Word] += 1