# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são
    os parâmetros de entrada e saída"""
    
    palavras = frase.split()
    result = frase.count(' ', 0, len(frase)) + 1
    
    if palavras[0] == ' ' and palavras[-1] == ' ':
        result = result - 2
        
    if palavras[0] == ' ' or palavras[-1] == ' ':
        result = result - 1
        
    return result