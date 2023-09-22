def quant_palavras(frase):
    """Dada um frase, a função retorna a quantidade de palavras
    nessa oração.
    	A frase deve ser escrita entre aspas.
        str --> int """
    frase = frase.strip()
    frase = frase.split()
    return len(frase)