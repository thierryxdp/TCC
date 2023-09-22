# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Recebe uma frase e retorna o número de palavras da frase.
     str -> int '''

    divisaoPalavras = str.split(frase)
    quantidadeP = len(divisaoPalavras)

    return quantidadeP