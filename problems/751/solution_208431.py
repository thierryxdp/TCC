# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna a quantidade de palavras da frase.
    string->int"""
    palavras_da_frase=str.split(frase)
    return len(palavras_da_frase)