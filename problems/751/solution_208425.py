# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    '''Função que, dada uma string "frase" de entrada, retorna o número
    "int" de palavras contidas na frase'''
    '''str -> int'''
    frase = str.split(frase)
    return len(frase)
# A função split divide um texto todas as vezes que a string passada
# passada como argumento for localizada