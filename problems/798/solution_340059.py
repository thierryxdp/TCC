def freq_palavras(frases):
    dicionario={}
    palavras=frases.split(' ')
    for string in palavras:
        indice=palavras.count(string)
        dicionario[string]=indice
    return dicionario# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis