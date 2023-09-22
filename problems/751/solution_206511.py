# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    'funcao que retorna o nmero de palavras de uma determinada frase'
    frase=str.split(frase)
    return len(frase)