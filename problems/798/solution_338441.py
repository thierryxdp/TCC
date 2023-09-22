# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """Função que dada uma string, ira retornar um dicionáio onde cada palavra é uma chave que tem como valor o número de vezes que a palavra aparece"""
    Dicionario = {}
    frase = frase.split(' ')
    for palavra in frase:
        if palavra not in Dicionario:
            Dicionario[palavra] = 1
        else:
            Dicionario[palavra] = Dicionario[palavra] + 1
    return Dicionario