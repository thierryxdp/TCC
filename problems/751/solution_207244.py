# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula a quantidade de palavras em uma frase; str =>int"""
    resp=frase.split()
    resp= len(resp)
    return resp