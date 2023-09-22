def quant_palavras(frase):
    """Função que retorna o número de palavras na frase. str --> int"""
    Fs_espaco = str.strip(frase)
    Nfrase = str.split(Fs_espaco)
    return len(Nfrase)