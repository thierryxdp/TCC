# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Essa função retorna o número de palavras de uma frase, considerando que a frase pode ter espaços no início e no final"""
    frase = str.split(frase)
    return len(frase)