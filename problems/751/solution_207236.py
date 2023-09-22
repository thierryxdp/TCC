# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ essa funcao recebe uma frase e retorna a quantidade de palavras que a na frase; str-> int"""
    x = len(str.split(frase))
    
    return x