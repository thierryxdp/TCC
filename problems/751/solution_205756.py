# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Funcao que calcula o numero de palavras de frase'''
    ''' str -> int '''
    var1 = str.split(frase)
    return len(var1)