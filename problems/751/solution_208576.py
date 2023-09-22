# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    #função que conta a quantidade de palavras em uma frase
    #string -> int
    lista_palavras = str.split(frase)
    return len(lista_palavras)