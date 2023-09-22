# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(palavras):
    palavras.split(" ")
    dicionario = {}
    for palavra in palavras:
        dicionario[palavra]=0
    for palavra in palavras:
        dicionario[palavra]+=1
    return dicionario