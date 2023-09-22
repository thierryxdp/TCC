def inverte (frase):
    """Função que dada uma frase, retorna a mesma na ordem inversa, sem letra maiuscula e sem pontuacao;
       str -> str."""
    frase_nova = str.lower (frase)
    frase_nova2 = str.replace (frase_nova, ",", " ")
    frase_nova3 = str.replace (frase_nova2, ":", " ")
    frase_nova4 = str.replace (frase_nova3, ";", " ")
    frase_nova5 = str.replace (frase_nova4, ".", " ")
    frase_nova6 = str.replace (frase_nova5, "!", " ")
    frase_nova7= str.replace (frase_nova6, "?", " ")
    frase_nova8= str.replace (frase_nova7, "...", " ")    
    frase_nova9= str.split (frase_nova8)
    frase_nova10= frase_nova9 [::-1]
    frase_nova11= str.join (" ", frase_nova10)
    return frase_nova11