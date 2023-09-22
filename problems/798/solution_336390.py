def freq_palavras(frases):
    """ Funcao que recebe uma string "frases" de entrada e retorna
    um dicionario, onde cada palavra dessa string é uma chave, e 
    seu valor respectivo e o numero de vezes que a palavra aparece na frase"""
    """str -> dict"""
    d={}
    for a in str.split(frases):
        if a in d:
            d[a] +=1
        else:
            d[a]=1
    return d
# Casos de teste:
""" freq_palavras("precisamos estudar precisamos entender")
>>> {'precisamos': 2, 'estudar,': 1, 'entender': 1}
    freq_palavras("temos que aprender a aprender")
>>> {'temos': 1, 'que': 1, 'aprender': 2, 'a': 1}
    freq_palavras("sempre bom melhorar, sempre bom")
>>> {'sempre': 2, 'bom': 2, 'melhorar,': 1} """