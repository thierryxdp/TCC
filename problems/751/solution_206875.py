# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Função que dada uma frase,retorne o número de palavras da frase.
    Parametro de entrada: string
    Valor de saida: int
    """
    s= str.split(frase)
    
    return len(s)