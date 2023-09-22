def sem_pontuacao (frase):
    """Função que dada uma frase, substitui todas as pontuacoes por espaços em branco;
       str -> str."""
    frase_nova = str.replace (frase, "-", " ")
    frase_nova2 = str.replace (frase_nova, ",", " ")
    frase_nova3 = str.replace (frase_nova2, ":", " ")
    frase_nova4 = str.replace (frase_nova3, ";", " ")
    frase_nova5 = str.replace (frase_nova4, ".", " ")
    frase_nova6 = str.replace (frase_nova5, "!", " ")
    frase_nova7= str.replace (frase_nova6, "?", " ")
    frase_nova8= str.replace (frase_nova7, "...", " ")
    return frase_nova8