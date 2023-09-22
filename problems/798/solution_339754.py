def freq_palavras(frases):
    '''função que recebe uma string e retorna um dicionário, no qual
    cada palavra da string seja uma chave e tenha como valor o número
    de vezes que essa palavra apareceu'''
    palavras = frases.split()
    dicionario = {}
    for i in palavras:
        contador = palavras.count(i)
        dicionario.update({i: contador})
    return dicionario