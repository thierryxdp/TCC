# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """uma função que dado uma frase, determina seu número de palavras:str->int"""
    a=str.split(frase)
    return len(a)