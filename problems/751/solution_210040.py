# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Essa função retorna o número de palavras de uma determinada frase,
    str->int. """
    frase = frase.strip(' ')
    palavras = frase.split(' ')
    resultado  = len(palavras)
    return resultado