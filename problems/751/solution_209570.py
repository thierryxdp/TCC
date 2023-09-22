# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''função que retorna a quantidade de palavras ultilizadas numa frase.
    split()'''
    sum([i.strip(string.punctuation).isalpha() for i in frase.split()])