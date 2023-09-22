# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorne a quantidade de palavras dado uma frase
    string - > int"""
    palavras = frase.split(" ")
    return len(palavras)