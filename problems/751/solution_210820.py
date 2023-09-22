# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
""" A função ira contar o numero de elementos dentro 'frase' 
string -> int """
def quant_palavras(frase):
    lista = frase.split()
    return len(lista)