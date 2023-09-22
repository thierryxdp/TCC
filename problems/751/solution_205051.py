# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''função que dada uma frase, retorne o númeor de palavras da frase.
    entrada: string
    saída: int'''
    return len(str.split(frase))