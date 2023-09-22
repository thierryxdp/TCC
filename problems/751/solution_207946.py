def quant_palavras(frase):
    """Retorna a quantidade de palavras da frase somando com os espaços entre elas e no final, caso haja também"""
#string -> int 
    quantidade = frase.split("")
    return len(quantidade)