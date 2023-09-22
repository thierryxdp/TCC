# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Conta a quantidade de palavras de uma frase" ; str ==> str"""
    frase= frase.split(' ')
    resp= len(frase)
    return resp