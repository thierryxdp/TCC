# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Esta função calcula o número de palavras que contém uma dada frase.
    Instruções: Informe a frase entre aspas como no exemplo
    ex.: 'Um pequeno passo para o homem, um grande salto para a humanidade'
    str -> int'''
    palavras = str.split(frase,' ')
    x = len(palavras)
    return x