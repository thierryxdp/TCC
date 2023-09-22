# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dado uma frase, retorna o numerro de palavras da frase"""
    palavras_frase=str.split(frase)
    return len(palavras_frase)