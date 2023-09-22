# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que conta a quantidade de palavras de uma frase"""
    ''' str -> int '''
    return (len(frase))/(str.count(frase, " "))