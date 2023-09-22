def freq_palavras(frases):
    '''função que retorna um dicionário onde cada palavra da string, dada
    como entrada, é uma chave e tem como valor o número de vezes
    que a palavra aparece
    string --> dict'''
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis