def freq_palavras(frase):
    palavras = frase.split()
    dicionario = {}
    for i in palavras:
        contador.count(i)
        dicionario.update({i: contador})
    return dicionario
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis