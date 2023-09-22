# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    dada uma string contendo uma frase, retorna  número de palavras da
    mesma
    """
    
    x=str.split(frase,' ')
    return len(x)