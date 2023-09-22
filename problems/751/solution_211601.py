# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe uma frase e retorna a quantidade de palavras
    Assinatura: string ---> int"""
    x = frase.split()
    return len(x)