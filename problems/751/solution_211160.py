# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''funcao que calcula a quantidade de palavras numa frase
    string->int'''
    lista=frase.split()
    return len(lista)