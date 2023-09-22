# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """  dada uma frase, retorne o número de palavras da frase. Considere que a frase pode ter espaços no início e no final.
    
    entrada-> str
    retonar-> int"""
    quant_palavras= str.split (frase)
    
    return list.count (quant_palavras,' ')