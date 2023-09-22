# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Conta quantas palavras estão presentes na frase dada.
    	str -> int
        
        Parameter:
        frase: String contendo a frase a ser contada.
        
        Returns:
        Quantidade de palavras na frase.
    """
    return len(frase.split())