def quant_palavras(frase):
    """funçao que dada uma frase retorna o numero de 
    palavras da frase; str->int"""
    frase_sem_espaco=str.strip(frase)
    return str.count(frase_sem_espaco, ' ') + 1