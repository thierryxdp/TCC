# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ função que retorna a quantidade de palavras
    contidas na frase a sua escolha.
    Assinatura: list --> int
    testes:
    quant_palavras(Olá) == 1
    quant_palavras(Olá Mundo) == 2
    quant_palavras(Olá Mundo Cruel) == 3
    """
    return len(str.split(frase))