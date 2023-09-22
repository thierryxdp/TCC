# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funçao que recebe uma frase e retorna o numero de palavras;
    str->int"""
    
    return str.count(frase,' ',0,-1)