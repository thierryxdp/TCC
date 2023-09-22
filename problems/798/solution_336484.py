# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    qtd_palavra = 1
    dicionario = {}
    for i in range(len(frases)):
        if frases.count(frases[i]) > 1:
            qtd_palavra = qtd_palavra*frases.count(frases[i])
        dicionario[frases[i]] = qtd_palavra
        return dicionario