def freq_palavras(frases):
    '''funcao que recebe uma frase e retorna um dicionario com as palavras e a quantidade de vezes que ela aparece na frase. str --> dict'''
    palavras = frases.split()
    dic = {}
    for palavra in palavras:
        dic = { palavra: palavras.count(palavra)}
    return dic