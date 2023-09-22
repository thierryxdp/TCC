# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada um frase, retorna a quantidade de palavras dentro dessa frase
    str->int"""
    frase_2=str.split(frase)
    quant_p=len(frase_2)
    
    return quant_p