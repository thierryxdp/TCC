# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Com str.split(), a string se separa nos espaços da frase retornando
    uma lista em que cada elemento é uma palavra. Com len(), descobre-se
    a quantidade de elementos dessa lista
    """
    
    frase = str.split(frase)
    return(len(frase))