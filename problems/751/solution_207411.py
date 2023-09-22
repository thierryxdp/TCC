# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    ''' função que retorna o número de palavras de uma frase,
    dados como entrada uma frase qualquer. str->int'''
    f_nova = str.strip(frase, ' ')
    return f_nova.count(' ') + 1