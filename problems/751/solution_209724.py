# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """utilizamos o str.split para separar cada palavra da Str,
    depois com o len contamos quantas palavras temos.
    str> str> int """
    
    palavras = str.split(frase)
    
    return len(palavras)