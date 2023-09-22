# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    str->int
    :param frase: Uma string
    :return : O tamanho em numeros das palavras contidas na frase
    """
    tamanho = int(len(frase.split()))
    return tamanho