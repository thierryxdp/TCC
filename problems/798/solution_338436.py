# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """Função que dada uma string, ira retornar um dicionáio onde cada palavra é uma chave que tem como valor o número de vezes que a palavra aparece"""
    Dicionario = {}
    frase = frase.split(' ')
    nova = []
    repetidos = []
    for palavra in frase:
        casa = 0
        if palavra in nova:
            repetidos.append(palavra)
            casa = casa + (len(repetidos))
        else:
            casa = casa + 1
            nova.append(palavra)
        Dicionario[palavra] = casa
    return Dicionario