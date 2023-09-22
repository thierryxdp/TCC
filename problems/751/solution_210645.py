# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dado uma frase, retorna a quantidade de palavras
    assinatura: string -> int
    testes:
    quant_palavras(bom dia) == 2
    quant_palavras( google ) == 1
    quant_palavras(dia ) == 1
    """
    return len(str.split(frase))