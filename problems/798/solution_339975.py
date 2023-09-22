# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    x=frases.split(' ')
    dicionario={}
    for i in x:
        dicionario[i]=x.count(i)
    return dicionario