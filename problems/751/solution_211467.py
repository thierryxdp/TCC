# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(x):
    '''função que calcula a quantidade de palavras em uma frase, que pode ter espaços no início e no final. 
    string -> int'''
    frase=x.strip()
    return frase.count(' ')+1