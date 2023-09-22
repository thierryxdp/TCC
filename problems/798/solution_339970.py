def freq_palavras(string):
    '''recebe um texto e retorna um dicionario onde cada
    palavra desse texto é uma chave e tenha como valor o numero de vezes
    que a palavra aparece
    str -> dicionario'''
    palavras = string.split()
    dicionario = {}

    for i in palavras:
        repeticao = palavras.count(i)
        dicionario[i] = repeticao
        
    return dicionario