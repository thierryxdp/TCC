# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna a quantidade de palavras em uma frase; str -> int """
    palavras = frase.split(" ")
    quantidade = len(palavras)
    return quantidade