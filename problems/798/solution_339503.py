# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
dicionario = {}
def freq_palavras(frases):
    lista = str.split(frases)
    for palavra in lista:
        if palavra not in dicionario:
            dicionario[palavra] = 0
        dicionario[palavras] += 1
        return dicionario