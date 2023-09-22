# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase:str)->int:
    """Dada uma frase, retorna o número de palavras da mesma."""
    return len(str.split(frase))