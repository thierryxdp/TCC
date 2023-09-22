# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Uma função que conta quantas palavras tem uma frase, dado o seu tamanho e contando seus espaçamentos e diminuindo um; str> int"""
    return len(str.split(frase))