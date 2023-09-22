# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
frequencia_palavras = {}

def freq_palavras(frases):
    """função que retorna um dicionário onde as chaves são strings e seus valores são equivalentes ao número de repeticoes"""
    lista = str.split(frases)
    for palavra in lista:
        if palavra not in frequencia_palavras:
            frequencia_palavras[palavra] = 0

        frequencia_palavras[palavra] +=1
    return frequencia_palavras