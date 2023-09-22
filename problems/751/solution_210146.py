# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """conta quantas palavras há em uma frase. 
    string -> int"""
    texto = frase
    contagem = len(texto.split())
    return contagem