# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    divisao=frases.split(' ')
    dicionario={}
    for contador in divisao:
        dicionario[contador]=divisao.count(contador)
    return dicionario