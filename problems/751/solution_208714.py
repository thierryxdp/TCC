# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o número de palavras de uma frase de entrada; str->int"""
    palavras= frase.split()
    return len(palavras)