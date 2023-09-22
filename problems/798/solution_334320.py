def freq_palavras(frase):
    '''Recebe uma string e retorna um dicionário onde cada palavra
    da string é a chave com o valor sendo o número de vezes que a
    palavra aparece; str -> dicionario'''
    palavras = str.split(frase)
    dicionario = {}
    for i in palavras:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario