# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula o número de palavras da frase, a partir do numero de espaços e pontos finaisnela"""
    quant_palavras = frase.split(' ') + frase.split('.')
    print (len(quant_palavras))