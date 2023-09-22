# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    frase = str.split(frases)
    dicionario = {}
    for palavra in frase:
    	contar = frase.count(palavra)
        dicionario[palavra]=contar
    return dicionario