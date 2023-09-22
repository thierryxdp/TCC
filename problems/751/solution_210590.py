# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Funcao que conta quantas palavras estão
    presentes em uma frase.
    str->int """
    lista_palavras = str.split(frase)
    return len(lista_palavras)