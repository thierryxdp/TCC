def freq_palavras(frases):
    '''funcao que recebe uma frase e retorna um dicionario com as palavras e a quantidade de vezes que ela aparece na frase. str --> dict'''
    palavras = frases.split()
    chaves = []
    values = []
    for palavra in palavras:
        
        values.append(palavras.count(palavra))
    return values