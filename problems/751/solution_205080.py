# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Esta função retorna o número de palavras contidas na frase.
       String --> int"""
    
    x = frase.split (" ")
    return len(x)