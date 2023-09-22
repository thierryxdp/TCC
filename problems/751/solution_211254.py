# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """str -> int"""
    """recebe uma frase e conta quantas palavras tem em uma frase"""
    
    Q = frase.count(' ') + 1
    
    if frase[0] == ' ' :
        Q -= 1
        pass
    
    if frase[-1] == ' ' :
        Q -= 1
        pass
    
    return Q