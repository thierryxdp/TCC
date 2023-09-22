def freq_palavras(frases):
    '''função que recebe uma string e retorna uma dicionário. onde cada palavra dessa string é uma chave e tem como valor o número de vezes que essa palavra aparece'''
    palavras = frases.split()
    dicionario = {}
    for palavra in palavras:
        dicionario[palavra] = palavras.count(palavra)    
    return dicionario