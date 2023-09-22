# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    ''' função que, dada uma frase, retorna o numero de palavras. Mesmo que tenha espaço no início e no final, estes não serão contabilizados.
str -> int '''
    return len(str(frase).strip())