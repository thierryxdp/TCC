# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Função que dada uma frase retorna o número de palavras da frase;
    obs: utilize espaço no começo e no final da frase;
    str->int'''
    return str.count(frase,' ',1)