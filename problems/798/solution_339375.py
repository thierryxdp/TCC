# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = str.split(frases)
    lista_freq = {}
    for palavra in palavras:
            lista_freq[palavra] = str.count(frases, palavra)
    return lista_freq