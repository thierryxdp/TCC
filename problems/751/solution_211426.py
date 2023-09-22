# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Assinatura: str-->int
    A função quant_palavras recebe uma frase em formato de string e 
    retorna um número int representando o número de palavras contidas
    nessa frase.
    """
    frase = str.split(frase)
    frase = len(frase)
    return frase