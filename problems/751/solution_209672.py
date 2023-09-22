# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    	A função retorna o número de palavras em uma frase, sendo cada palavra
        separada por espaços e a entrada é essa frase.
        frase -> str
        str -> int
    """
    a=str.split(frase)
    return len(a)