# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Recebe uma frase e retorna a quantidade de palavras contidas nela
    string -> lista -> len(lista)"""
    palavras = frase.split()
    return len(palavras)