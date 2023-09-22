# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """Função que dada uma string, ira retornar um dicionáio onde cada palavra é uma chave que tem como valor o número de vezes que a palavra aparece"""
    lista = []
    lissta = []
    Dicionario = {}
    frase = frase.split(' ')
    for palavra in frase:
        lista.append(palavra)
        Dicionario[palavra] = 1
    return dicionario