# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
    A função retorna o número de palavras de uma frase
    (entrada = str / saída = str)
    '''
    return len(str.split(str.strip(frase)))