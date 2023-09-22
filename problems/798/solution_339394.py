# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = []
    palavras = str.split(frases)
    lista_freq = {}
    contador = 0
    for palavra in palavras:
        if palavras[contador] == palavra:
            lista_freq[palavra] += 1
        contador += 0
    return lista_freq