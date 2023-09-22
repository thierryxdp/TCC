# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    x = str.split(frase)
    dicionario = {}
    for x[i] in x:
        if x[i] in dicionario:
            dicionario[x[i]] += 1 
        else:
            dicionario[x[i]] = 1
    return dicionario