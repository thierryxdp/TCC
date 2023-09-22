# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Conta a quantidade de palavras em uma string.
       str->int
       
       Parameters:
       frase: A string da qual as palavras vão ser contadas.
       
       Returns:
       O número de palavras de uma string."""
    y=str.split(frase,' ')
    return len(y)