def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário no qual cada palavra da string é uma chave e tem como valor o número de vezes que a palavra apareceu.
    str -> dicionário'''
    palavras - frases.split()
    dicionario = {}
    
    for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i: contador})
    return dicionario