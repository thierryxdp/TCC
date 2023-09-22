# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Recebe uma frase e retorna o número de palavras na mesma.
    string -> int'''

    s = frase
    c = str.split(s)
    
    return len(c)