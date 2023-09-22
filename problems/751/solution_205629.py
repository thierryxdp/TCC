def quant_palavras (frase):
    """Função que recebe uma frase e retorna o número de palavras da mesma, considerando a frase possa ter espaços no ínicio e no final
    entrada: string
    saída: int"""
    return str.split(frase, ',', '.', '!', ';')