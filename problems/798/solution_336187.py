# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = frases.split()
    frequencia = {x : palavras.count(x) for x in palavras}
    return frequencia