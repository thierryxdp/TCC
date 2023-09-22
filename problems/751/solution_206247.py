# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Ao fornecer uma frase, retorna a quantidade de palavras presentes na mesma"""
    """ str -> int"""


    lista = str.split(str(frase), ' ')
    return len(lista)