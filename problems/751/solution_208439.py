# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que dada uma frase, retorna a quantidade
    de palavras dessa frase.
    str -> int"""
    return len(str.split(frase))
#Casos de teste
#frase('comi bolo e pudim na festa, acabei passando mal') == 9
#frase(' ') == 0