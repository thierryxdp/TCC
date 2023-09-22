# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
 """recebe uma frase e retorna o numero de palavras q a mesma possui,string -> int"""
def quant_palavras(frase):
    
    frase = frase.split()
    return sum(frase)