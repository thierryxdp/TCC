# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe uma frase e retorna o número de palavras que esta frase 
    contém"""
    num_palavras = frase.split(' ')
    return len(num_palavras)