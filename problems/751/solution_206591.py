"""Antes de tudo, vamos transformar nossa função em uma lista onde os espaços em branco são removidos. Após isso, basta ver o tamanho da nossa lista - chamando len - para sabermos o número de palavras."""


def quant_palavras(frase):
    """Função que dada uma frase, retorna o número de palavras da frase.
    str -> int """

    palavras = frase.split()
    return len(palavras)