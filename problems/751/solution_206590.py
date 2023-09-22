# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o número de palavras de uma frase dado uma frase.
    str -> int
    
    exemplos:
    quant_palavras("sasa aaasasf asasa")==3
    """
    return len(str.split(frase))