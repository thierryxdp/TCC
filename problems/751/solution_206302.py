# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A funcao recebe uma frase e retorna a quantidade de palavras da frase, considerando
    que a frase pode ter espacos no inicio e no final.
    Parametro de entrada:str
    Valor de retorno: int"""
    frase=str.rstrip(frase)
    frase=str.lstrip(frase)
    return(len(str.split(frase," ")))