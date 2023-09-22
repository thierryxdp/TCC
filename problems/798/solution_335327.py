# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''dada uma string (frases), retorna um dicionario,
    onde cada palavra dessa string seja uma cheve e
    tenha como valor o numero de vezes que a palavra
    é repetida; str -> dict'''
    frases2 = str.split(frases)
    palavras = {}
    for posicao in frases2:
        if posicao not in palavras:
            palavras[posicao] = 1
        else:
            palavras[posicao] += 1

    return palavras