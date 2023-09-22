# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Essa função retorna a quantidade de palavras da frase dada como entrada"""
    lista = frase.split(' ')
    lista_nova = list.count(lista)
    return lista_nova