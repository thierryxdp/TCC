# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """Função que dada uma string, ira retornar um dicionáio onde cada palavra é uma chave que tem como valor o número de vezes que a palavra aparece"""
    Dicionario = {}
    frase = frase.split(' ')
    nova = []
    for palavra in frase:
        casa = 1
        if palavra in nova:
            casa = casa + casa
        else:
            casa = casa
            nova.append(palavra)
        Dicionario[palavra] = casa
    return Dicionario