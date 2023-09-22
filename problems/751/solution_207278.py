# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada um frase retorna onumero de palavras;
str->int"""
    x=len(str.split(frase," "))
    return x