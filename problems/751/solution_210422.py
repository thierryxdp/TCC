# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o número palavras dentro de uma frase.
    Testes: quant_palavras('um') == 1
    quant_palavras('um dois') == 2
    assinatura: str --> int
    """
    return len(str.split(frase))