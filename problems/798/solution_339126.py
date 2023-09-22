# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    palavras = frases.split()
    dicionario = {}
    count = 1
    for palavra in palavras:
        dicionario[count] = palavra
        count += 1
      
    return dicionario