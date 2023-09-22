# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    def quant_palavras(frase):
    '''função que retorna o numero de palavras da frase sem contar
    os espaços'''
    frase = frase.strip()
    frase = frase.split()
    return len(frase)