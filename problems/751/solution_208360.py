def quant_palavras(frase):
    """
    Função que recebe uma frase qualquer. Separa a frase em 
    elementos de uma lista com o termo divisor sendo o espaço.
    Após isso, retorna a quantidade de elementos desta lista.
    Cada elemento é uma palavra da frase. str -> int
    """
    return len(frase.split())