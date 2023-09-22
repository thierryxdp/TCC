# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase:str)->int:
    """Função que retorna a quantidade de palavras em uma frase"""
    x= str.split(frase)
    return len(x)