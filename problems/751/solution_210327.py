# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """retorna o número de palavras da frase; tem como entrada a frase;str->str) """
     frase = str.split(frase)
     return len(frase)