# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = []
    for x in frases:
        palavras.append(x) 
    frequencia = {x : palavras.count(x) for x in palavras}
    return frequencia