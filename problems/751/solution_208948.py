# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """a função toma como entrada uma frase, separa ela por espaços e depois conta"""
    separa=frase.split(" ")
    return len(separa)