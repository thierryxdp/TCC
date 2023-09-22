def freq_palavras(frases):
    '''função que recebe uma string como entrada
    retorna um dicionário onde cada palavra dessa
    string seja uma chave e tenha como valor o número
    de vezes que a palavra aparece
    str-->dici'''
    dici = {}
    palavras = str.split(frases)
    for palavra in palavras:
        cont = list.count(palavras, palavra)
        dici[palavra]=cont
    return dici