# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao retorna quantas palavras existem em uma frase, dada
    na forma de string: frase """

    p = frase.split(" ")
    
    return len(p)