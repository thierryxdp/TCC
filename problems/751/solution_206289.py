# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Informa quantas palavras têm na string informada
    Parametros:
    	frase -> str
        frase a ser analisada
    Returns:
    	int
        número de palavras
    """
    n=str.split(frase)
    return len(n)