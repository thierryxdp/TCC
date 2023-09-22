# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que conta palavras de uma frase.
    string -> int"""
    contagem = frase.split(" ")
    
    return len(contagem)