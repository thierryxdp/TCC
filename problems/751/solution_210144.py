# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A função retorna a quantidade de palavras dentro de uma string denominada "frase" ."""
    cont = 0
    lista = frase.split()
    for c in lista:
        cont +=1
    return cont