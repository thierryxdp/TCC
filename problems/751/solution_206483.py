# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que recebe uma frase e retorna a quantidade de palavras na frase
       parâmetro de entrada:str
       parâmetro de saída: int"""
    return len(str.split(frase))